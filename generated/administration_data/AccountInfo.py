import requests, json
from generated.base.unit4_base import Unit4Base
class AccountInfo(Unit4Base):


    def get_{fiscalYear}_{schemaId}_byFiscalyear_and_schemaId_and_fiscalYear_and_schemaId_and_type(self, database, fiscalYear, schemaId, type, ):
        request_args = locals()
        url_template = 'api/{database}/AccountInfoList/NotLinkedAccounts/{fiscalYear}/{schemaId}/{type}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_accountInfoList_byFiscalyear_and_accountId(self, database, fiscalYear, accountId, ):
        request_args = locals()
        url_template = 'api/{database}/AccountInfoList/{fiscalYear}?accountId={accountId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_accountInfoList_byFiscalyear(self, database, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/AccountInfoList/{fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    