import requests, json
from generated.base.unit4_base import Unit4Base
class JournalEntryLineInfo(Unit4Base):


    def get_{fiscalYear}_{startDate}_byFiscalyear_and_startDate_and_fiscalYear_and_startDate_and_endDate_and_accountid(self, database, fiscalYear, startDate, endDate, accountid, ):
        request_args = locals()
        url_template = 'api/{database}/JournalEntryLineInfoList/ByDate/{fiscalYear}/{startDate}/{endDate}?accountid={accountid}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{fiscalYear}_{startDate}_byFiscalyear_and_startDate_and_fiscalYear_and_startDate_and_endDate(self, database, fiscalYear, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/JournalEntryLineInfoList/ByDate/{fiscalYear}/{startDate}/{endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{fiscalYear}_{startPeriod}_byFiscalyear_and_startPeriod_and_fiscalYear_and_startPeriod_and_endPeriod_and_accountId(self, database, fiscalYear, startPeriod, endPeriod, accountId, ):
        request_args = locals()
        url_template = 'api/{database}/JournalEntryLineInfoList/ByPeriod/{fiscalYear}/{startPeriod}/{endPeriod}?accountId={accountId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{fiscalYear}_{startPeriod}_byFiscalyear_and_startPeriod_and_fiscalYear_and_startPeriod_and_endPeriod(self, database, fiscalYear, startPeriod, endPeriod, ):
        request_args = locals()
        url_template = 'api/{database}/JournalEntryLineInfoList/ByPeriod/{fiscalYear}/{startPeriod}/{endPeriod}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_journalEntryLineInfoList_byFiscalyear_and_accountid(self, database, fiscalYear, accountid, ):
        request_args = locals()
        url_template = 'api/{database}/JournalEntryLineInfoList/OpeningBalance/{fiscalYear}?accountid={accountid}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_journalEntryLineInfoList_byFiscalyear(self, database, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/JournalEntryLineInfoList/OpeningBalance/{fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{period}_{accountid}_byFiscalyear_and_period_and_fiscalYear_and_period_and_accountid(self, database, fiscalYear, period, accountid, ):
        request_args = locals()
        url_template = 'api/{database}/JournalEntryLineInfoList/{fiscalYear}/{period}/{accountid}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    