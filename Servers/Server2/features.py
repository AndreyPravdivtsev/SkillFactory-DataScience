import numpy as np
import json
from sklearn.datasets import load_diabetes
import pika
# start in the other terminal
# sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
X, y = load_diabetes(return_X_y=True)
random_row = np.random.randint(0, X.shape[0]-1)

print(f'Random diabetes row is {random_row}')

# Подключение к серверу на локальном хосте:
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создадим очередь, с которой будем работать:
# Опубликуем сообщение
# exchange определяет, в какую очередь отправляется сообщение. Если мы используем дефолтную точку обмена, то значение можно оставить пустым.
# параметр routing_key указывает имя очереди, 
# параметр body тело самого сообщения, 

channel.queue_declare(queue='y_true')
message = list(y)[random_row]
message_serial = json.dumps(message)
channel.basic_publish(exchange='',
                      routing_key='y_true',
                      body=message_serial)
print(f'Random diabetes value {message}')
print(f'Random diabetes serialized value {message_serial}')

channel.queue_declare(queue='Features')
message = list(X[random_row])
message_serial = json.dumps(message)
channel.basic_publish(exchange='',
                      routing_key='Features',
                      body=message_serial)
print(f'Random diabetes features {message}')
print(f'Random diabetes serialized features {message_serial}')

print('Сообщение с правильным ответом, отправлено в очередь')
# Закроем подключение 
connection.close()
