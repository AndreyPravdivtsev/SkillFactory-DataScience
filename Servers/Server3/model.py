# Скрипт загрузки модели, прослушивания очереди в RabbitMQ,
# предикта и отправки предиктов в соответствующую очередь
# Пример из "6. Сервис II"

import pika
import json
import pickle
import numpy as np

MODEL_FILE_PATH = './myfile.pkl'

with open(MODEL_FILE_PATH, 'rb') as pkl_file:
    regressor = pickle.load(pkl_file)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Features')
channel.queue_declare(queue='y_pred')


def make_predict(body):
    # Десериализуем данные
    data = json.loads(body)

    # Делаем предикт
    y_pred = regressor.predict(np.array(data).reshape(1, -1))

    # Сериализуем предикт
    y_pred_ser = json.dumps(y_pred.tolist()[0])

    return y_pred_ser


def callback(ch, method, properties, body):
    print(f'Получен вектор признаков {body}')

    y_pred_ser = make_predict(body)

    ch.basic_publish(exchange='',
                     routing_key='y_pred',
                     body=y_pred_ser)

    print(f'Предикт отправлен {y_pred_ser}')


# on_message_callback показывает какую функцию вызвать при получении сообщения
channel.basic_consume(
    queue='Features',
    on_message_callback=callback,
    auto_ack=True)

print('...Ожидание сообщений, для выхода нажмите CTRL+C')

channel.start_consuming()