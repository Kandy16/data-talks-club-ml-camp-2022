
from flask import Flask
from flask import request, jsonify

from solution_question3 import predict_card_issue

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    print('Reached root')
    return 'root response'

@app.route('/predict',methods=['POST'])
def predict_credit_card_issue():
    customer = request.get_json()
    card_issue_prob = predict_card_issue(customer)
    response_dict = {
        'card_issue_probability':card_issue_prob,
        'card_issued':bool(card_issue_prob >= 0.5)
    }

    print(response_dict)

    return jsonify(response_dict)



