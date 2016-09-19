import requests, json
from generated.base.unit4_base import Unit4Base
class AccountNVL(Unit4Base):


    def get_accountNVL_byFiscalyear(self, database, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/AccountNVL/WithProjectAccounts/{fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_accountNVL_byFiscalyear(self, database, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/AccountNVL?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_accountNVL(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/AccountNVL'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    