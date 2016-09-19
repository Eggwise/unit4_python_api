import requests, json
from generated.base.unit4_base import Unit4Base
class Product(Unit4Base):


    def delete_product_byProductid(self, database, productId, ):
        request_args = locals()
        url_template = 'api/{database}/Product/{productId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_product_byProductid(self, database, productId, ):
        request_args = locals()
        url_template = 'api/{database}/Product/{productId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_product(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Product'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_product_byProductid(self, database, productId, ):
        request_args = locals()
        url_template = 'api/{database}/Product/{productId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    