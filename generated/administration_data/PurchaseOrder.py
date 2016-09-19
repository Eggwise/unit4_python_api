import requests, json
from generated.base.unit4_base import Unit4Base
class PurchaseOrder(Unit4Base):


    def delete_purchaseOrder_byOrderid(self, database, orderId, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseOrder/{orderId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_purchaseOrder_byOrderid(self, database, orderId, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseOrder/{orderId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_purchaseOrder(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseOrder'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_purchaseOrder_byOrderid(self, database, orderId, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseOrder/{orderId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    