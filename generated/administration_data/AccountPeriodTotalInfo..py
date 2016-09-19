import requests, json
from generated.base.unit4_base import Unit4Base
class AccountPeriodTotalInfo.(Unit4Base):


    def get_{fiscalYear}_{accountId}_byFiscalyear_and_accountId(self, database, fiscalYear, accountId, ):
        request_args = locals()
        url_template = 'api/{database}/AccountPeriodTotalInfo/OpeningBalance/{fiscalYear}/{accountId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{periodId}_{accountId}_byFiscalyear_and_periodId_and_fiscalYear_and_periodId_and_accountId(self, database, fiscalYear, periodId, accountId, ):
        request_args = locals()
        url_template = 'api/{database}/AccountPeriodTotalInfo/{fiscalYear}/{periodId}/{accountId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    