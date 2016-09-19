import requests, json
from generated.base.unit4_base import Unit4Base
class Account(Unit4Base):


    def delete_account_byFiscalyear_and_accountId(self, database, fiscalYear, accountId, ):
        request_args = locals()
        url_template = 'api/{database}/Account/{fiscalYear}/{accountId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_account_byFiscalyear_and_accountId(self, database, fiscalYear, accountId, ):
        request_args = locals()
        url_template = 'api/{database}/Account/{fiscalYear}/{accountId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_account(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Account'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_account_byFiscalyear_and_accountId(self, database, fiscalYear, accountId, ):
        request_args = locals()
        url_template = 'api/{database}/Account/{fiscalYear}/{accountId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    