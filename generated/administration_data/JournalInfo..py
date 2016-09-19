import requests, json
from generated.base.unit4_base import Unit4Base
class JournalInfo.(Unit4Base):


    def get_journalInfo_byJournalid_and_fiscalYear(self, database, journalId, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/JournalInfo/{journalId}?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_journalInfo_byJournalid(self, database, journalId, ):
        request_args = locals()
        url_template = 'api/{database}/JournalInfo/{journalId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    