import requests, json
from generated.base.unit4_base import Unit4Base
class Customer(Unit4Base):


    def delete_customer_byCustomerid(self, database, customerId, ):
        request_args = locals()
        url_template = 'api/{database}/Customer/CustomerAndOrganization/{customerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def delete_customer_byCustomerid(self, database, customerId, ):
        request_args = locals()
        url_template = 'api/{database}/Customer/{customerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_customer_byCustomerid(self, database, customerId, ):
        request_args = locals()
        url_template = 'api/{database}/Customer/{customerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_customer(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Customer'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_customer_byCustomerid(self, database, customerId, ):
        request_args = locals()
        url_template = 'api/{database}/Customer/{customerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    