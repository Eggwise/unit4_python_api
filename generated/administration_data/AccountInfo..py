import requests, json
from generated.base.unit4_base import Unit4Base
class AccountInfo.(Unit4Base):


    def get_accountInfo_byAccountid_and_fiscalYear(self, database, accountId, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/AccountInfo/{accountId}?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_accountInfo_byAccountid(self, database, accountId, ):
        request_args = locals()
        url_template = 'api/{database}/AccountInfo/{accountId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    