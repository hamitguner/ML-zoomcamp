import pickle 

from flask import Flask
from flask import request
from flask import jsonify

with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('Payment')


@app.route('/predict', methods =['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    result = y_pred >= 0.5

    result = {
        'payment_probability' : float(y_pred),
        'result' : bool(result)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 9696)