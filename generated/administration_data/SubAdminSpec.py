import requests, json
from generated.base.unit4_base import Unit4Base
class SubAdminSpec(Unit4Base):


    def get_subAdminSpecList_byFiscalyear_and_accountId(self, database, fiscalYear, accountId, ):
        request_args = locals()
        url_template = 'api/{database}/SubAdminSpecList/{fiscalYear}/{accountId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    