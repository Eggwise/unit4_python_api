import requests, json
from generated.base.unit4_base import Unit4Base
class Order(Unit4Base):


    def delete_order_byOrderid(self, database, orderId, ):
        request_args = locals()
        url_template = 'api/{database}/Order/{orderId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_order_byOrderid(self, database, orderId, ):
        request_args = locals()
        url_template = 'api/{database}/Order/{orderId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_order(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Order'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_order_byOrderid(self, database, orderId, ):
        request_args = locals()
        url_template = 'api/{database}/Order/{orderId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    