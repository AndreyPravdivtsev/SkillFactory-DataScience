# Скрипт отправки признаков и истинных меток.
# Пример из "5. Сервис I"

# перед запуском features.py (командой "python features.py")
# нужно запустить RabbitMQ в докер контейнере:
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

import pika
import json
import numpy as np
from sklearn.datasets import load_diabetes


X, y = load_diabetes(return_X_y=True)
random_row = np.random.randint(0, X.shape[0]-1)

# Сериализация
y_ser = json.dumps(y[random_row])
x_ser = json.dumps(X[random_row].tolist())

# Подключение к серверу на локальном хосте:
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создадим очередь, с которой будем работать:
channel.queue_declare(queue='y_true')
channel.queue_declare(queue='Features')


# Опубликуем сообщение
# exchange определяет, в какую очередь отправляется сообщение,
# параметр routing_key указывает имя очереди,
# параметр body тело самого сообщения,
channel.basic_publish(exchange='',
                      routing_key='y_true',
                      body=y_ser)
channel.basic_publish(exchange='',
                      routing_key='Features',
                      body=x_ser)

print('Сообщение с правильным ответом, отправлено в очередь')
# Закроем подключение
connection.close()