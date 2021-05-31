import pika
import numpy as np
from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True)
random_row = np.random.randint(0, X.shape[0]-1)