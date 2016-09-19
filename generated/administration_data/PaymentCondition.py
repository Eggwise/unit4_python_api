import requests, json
from generated.base.unit4_base import Unit4Base
class PaymentCondition(Unit4Base):


    def delete_paymentCondition_byPaymentconditionid(self, database, paymentConditionId, ):
        request_args = locals()
        url_template = 'api/{database}/PaymentCondition/{paymentConditionId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_paymentCondition_byPaymentconditionid(self, database, paymentConditionId, ):
        request_args = locals()
        url_template = 'api/{database}/PaymentCondition/{paymentConditionId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_paymentCondition(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/PaymentCondition'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_paymentCondition_byPaymentconditionid(self, database, paymentConditionId, ):
        request_args = locals()
        url_template = 'api/{database}/PaymentCondition/{paymentConditionId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    