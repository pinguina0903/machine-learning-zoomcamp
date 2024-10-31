import pickle

from flask import Flask
from flask import request
from flask import jsonify

with open("model1.bin", "rb") as f_in:
    model = pickle.load(f_in)

with open("dv.bin", "rb") as f_in:
    dv = pickle.load(f_in)


app = Flask('suscription')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    suscription = y_pred >= 0.5

    result = {
        'suscription_probability': float(y_pred),
        'suscription': bool(suscription)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)