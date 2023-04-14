from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__)
@app.route('/api/changed', methods=['GET', 'POST', 'DELETE'])
def changed():
    #get the csv as dict. Not the most beautiful choise but gets the csv
    if request.method == 'GET':
        df = pd.read_csv('changed1.csv')
        return {'Changed': df.to_dict()}, 200

    if request.method == 'POST':
        # insert new row in dataframe
        df = pd.read_csv('changed1.csv')
        data = request.get_json()
        changed = [data['day'], data['personnel'], data['POW']]
        df = df.append(pd.Series(changed, index=df.columns), ignore_index=True)
        df.to_csv('changed1.csv', index=False)







if __name__ == '__main__':
    app.run(debug=True)
