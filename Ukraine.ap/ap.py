from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__)
@app.route('/api/changed', methods=['GET', 'POST', 'DELETE'])
def changed():
    #get the csv as dict. Not the most beautiful choise but gets the csv
    if request.method == 'GET':
        df = pd.read_csv('changed.csv')
        return {'Changed': df.to_dict()}, 200


if __name__ == '__main__':
    app.run(debug=True)