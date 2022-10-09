import pickle
import os

parent_directory = os.path.dirname(os.path.realpath(__file__))
#parent_directory = os.path.dirname(parent_directory)
with open(os.path.join(parent_directory, 'dv.bin'), mode='rb') as dv_handle:
    dv = pickle.load(dv_handle)

with open(os.path.join(parent_directory, 'model1.bin'), mode='rb') as model_handle:
    model = pickle.load(model_handle)


def predict_card_issue(customer):
    customer_dict = dv.transform(customer)
    customer_predict = model.predict_proba(customer_dict)[0,1]
    return customer_predict

if __name__ == '__main__':
    customer = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
    result = predict_card_issue(customer)
    print(f'For the customer - {customer}, the prediction probablity for issuing a card is : {result}')

