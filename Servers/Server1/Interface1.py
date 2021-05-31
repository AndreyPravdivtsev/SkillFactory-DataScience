import pika
import numpy as np
import json
from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True)
random_row = np.random.randint(0, X.shape[0]-1)

# Подключение к серверу на локальном хосте:
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создадим очередь, с которой будем работать:
channel.queue_declare(queue='y_true')

# Опубликуем сообщение
# exchange определяет, в какую очередь отправляется сообщение. Если мы используем дефолтную точку обмена, то значение можно оставить пустым.
# параметр routing_key указывает имя очереди, 
# параметр body тело самого сообщения, 

message = list(y[random_row])
message_serial = json.dumps(message)

channel.basic_publish(exchange='',
                      routing_key='y_true',
                      body=message_serial)
print('Сообщение с правильным ответом, отправлено в очередь')
# Закроем подключение 
connection.close()