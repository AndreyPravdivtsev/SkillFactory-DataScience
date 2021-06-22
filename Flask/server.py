import pickle
from datetime import datetime
import numpy as np
import sklearn
from flask import Flask, request, jsonify


app = Flask(__name__)

with open('hw1.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

@app.route("/hello")
def hello_func():
    name = request.args.get("name")
    id = request.args.get("id")
    return f"hello, {name} with id {id}!", 200

# http://localhost:5000/hello?name=world&id=2

@app.route('/time')
def current_time():
    return {'time': datetime.now()}, 200



@app.route("/add",methods=["POST"])
def add_func():
    num = request.json.get("num")
    if num > 10:
        return "too much", 400
    return jsonify({"result":num+1})

# Задание 7.2
@app.route('/predict', methods=['POST'])
def predict():
    numbers = request.json  # .get('numbers')
    # print(numbers)
    result = model.predict(np.array(numbers).reshape(1, -1))
    return jsonify({'prediction': result[0]})


if __name__ == "__main__":
    app.run("localhost",5000)



    #subprocess.call(['python3.8', '../client.py'])