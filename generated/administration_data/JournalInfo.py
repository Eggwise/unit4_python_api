import requests, json
from generated.base.unit4_base import Unit4Base
class JournalInfo(Unit4Base):


    def get_journalInfoList_byFiscalyear_and_types(self, database, fiscalYear, types, ):
        request_args = locals()
        url_template = 'api/{database}/JournalInfoList/{fiscalYear}?types={types}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_journalInfoList_byTypes_and_fiscalYear(self, database, types, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/JournalInfoList?types={types}&amp;fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_journalInfoList_byFiscalyear(self, database, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/JournalInfoList?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_journalInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/JournalInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    