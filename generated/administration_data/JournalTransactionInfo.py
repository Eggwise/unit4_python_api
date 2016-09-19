import requests, json
from generated.base.unit4_base import Unit4Base
class JournalTransactionInfo(Unit4Base):


    def get_{journalId}_{startDate}_byJournalid_and_startDate_and_journalId_and_startDate_and_endDate(self, database, journalId, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/JournalTransactionInfoList/Range/{journalId}/{startDate}/{endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_journalTransactionInfoList_byJournalid_and_fiscalYear(self, database, journalId, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/JournalTransactionInfoList/{journalId}/{fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    