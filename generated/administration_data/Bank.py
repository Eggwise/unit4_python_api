import requests, json
from generated.base.unit4_base import Unit4Base
class Bank(Unit4Base):


    def delete_bank_byBankid(self, database, bankId, ):
        request_args = locals()
        url_template = 'api/{database}/Bank/{bankId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_bank_byBankid(self, database, bankId, ):
        request_args = locals()
        url_template = 'api/{database}/Bank/{bankId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_bank(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Bank'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_bank_byBankid(self, database, bankId, ):
        request_args = locals()
        url_template = 'api/{database}/Bank/{bankId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    