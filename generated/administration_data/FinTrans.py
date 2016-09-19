import requests, json
from generated.base.unit4_base import Unit4Base
class FinTrans(Unit4Base):


    def delete_{journalId}_{journalTransaction}_byFiscalyear_and_journalId_and_fiscalYear_and_journalId_and_journalTransaction(self, database, fiscalYear, journalId, journalTransaction, ):
        request_args = locals()
        url_template = 'api/{database}/FinTrans/{fiscalYear}/{journalId}/{journalTransaction}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{journalId}_{journalTransaction}_byFiscalyear_and_journalId_and_fiscalYear_and_journalId_and_journalTransaction(self, database, fiscalYear, journalId, journalTransaction, ):
        request_args = locals()
        url_template = 'api/{database}/FinTrans/{fiscalYear}/{journalId}/{journalTransaction}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_finTrans(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/FinTrans'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_{journalId}_{journalTransaction}_byFiscalyear_and_journalId_and_fiscalYear_and_journalId_and_journalTransaction(self, database, fiscalYear, journalId, journalTransaction, ):
        request_args = locals()
        url_template = 'api/{database}/FinTrans/{fiscalYear}/{journalId}/{journalTransaction}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    