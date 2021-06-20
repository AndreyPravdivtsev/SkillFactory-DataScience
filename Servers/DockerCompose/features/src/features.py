import pika
import json
import numpy as np
import time
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)

while True:
	try:
		random_row = np.random.randint(0, X.shape[0]-1)

		connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
		channel = connection.channel()

		channel.queue_declare(queue='Features')
		channel.queue_declare(queue='y_true')

		channel.basic_publish(exchange='',
		                      routing_key='Features',
		                      body=json.dumps(list(X[random_row])))
		print('Сообщение с вектором признаков, отправлено в очередь')

		channel.basic_publish(exchange='',
		                      routing_key='y_true',
		                      body=json.dumps(y[random_row]))

		print('Сообщение с правильным ответом, отправлено в очередь')
		connection.close()
		time.sleep(2)
	except:
		print('Не удалось подключиться к очереди')

