import pika
import pickle
import numpy as np


# Возьмём файл с обученной моделью из модуля 1:
with open('myfile.pkl', 'rb') as pkl_file:
    regressor = pickle.load(pkl_file)


# Подключимся к серверу:

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# queue
channel.queue_declare(queue='Features')

def callback(ch, method, properties, body):
    print(f'Получен вектор признаков {body}')
	
# on_message_callback показывает какую функцию вызвать при получении сообщения
channel.basic_consume(
    queue='Features', on_message_callback=callback, auto_ack=True)
print('...Ожидание сообщений, для выхода нажмите CTRL+C')


channel.start_consuming()