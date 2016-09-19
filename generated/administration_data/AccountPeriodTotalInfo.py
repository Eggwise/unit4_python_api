import requests, json
from generated.base.unit4_base import Unit4Base
class AccountPeriodTotalInfo(Unit4Base):


    def get_{fiscalYear}_{accountId}_byFiscalyear_and_accountId(self, database, fiscalYear, accountId, ):
        request_args = locals()
        url_template = 'api/{database}/AccountPeriodTotalInfoList/ByAccountId/{fiscalYear}/{accountId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{fiscalYear}_{startPeriod}_byFiscalyear_and_startPeriod_and_fiscalYear_and_startPeriod_and_endPeriod(self, database, fiscalYear, startPeriod, endPeriod, ):
        request_args = locals()
        url_template = 'api/{database}/AccountPeriodTotalInfoList/ByPeriod/{fiscalYear}/{startPeriod}/{endPeriod}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_accountPeriodTotalInfoList_byFiscalyear(self, database, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/AccountPeriodTotalInfoList/{fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    