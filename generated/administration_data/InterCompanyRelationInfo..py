import requests, json
from generated.base.unit4_base import Unit4Base
class InterCompanyRelationInfo.(Unit4Base):


    def get_{journalId}_{targetAdministration}_byFiscalyear_and_journalId_and_fiscalyear_and_journalId_and_targetAdministration(self, database, fiscalyear, journalId, targetAdministration, ):
        request_args = locals()
        url_template = 'api/{database}/InterCompanyRelationInfo/{fiscalyear}/{journalId}/{targetAdministration}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    