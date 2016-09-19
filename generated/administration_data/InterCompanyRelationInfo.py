import requests, json
from generated.base.unit4_base import Unit4Base
class InterCompanyRelationInfo(Unit4Base):


    def get_interCompanyRelationInfoList_byFiscalyear_and_sourceJournal(self, database, fiscalYear, sourceJournal, ):
        request_args = locals()
        url_template = 'api/{database}/InterCompanyRelationInfoList/{fiscalYear}/{sourceJournal}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    