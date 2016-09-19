import requests, json
from generated.base.unit4_base import Unit4Base
class DeliveryCondition(Unit4Base):


    def delete_deliveryCondition_byDeliveryconditionid(self, database, deliveryConditionId, ):
        request_args = locals()
        url_template = 'api/{database}/DeliveryCondition/{deliveryConditionId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_deliveryCondition_byDeliveryconditionid(self, database, deliveryConditionId, ):
        request_args = locals()
        url_template = 'api/{database}/DeliveryCondition/{deliveryConditionId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_deliveryCondition(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/DeliveryCondition'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_deliveryCondition_byDeliveryconditionid(self, database, deliveryConditionId, ):
        request_args = locals()
        url_template = 'api/{database}/DeliveryCondition/{deliveryConditionId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    