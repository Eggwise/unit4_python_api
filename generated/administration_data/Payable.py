import requests, json
from generated.base.unit4_base import Unit4Base
class Payable(Unit4Base):


    def get_payableList_byState(self, database, state, ):
        request_args = locals()
        url_template = 'api/{database}/PayableList/ByState/{state}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_payableList_byBankid(self, database, bankId, ):
        request_args = locals()
        url_template = 'api/{database}/PayableList/{bankId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_payableList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/PayableList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    