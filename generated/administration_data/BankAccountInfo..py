import requests, json
from generated.base.unit4_base import Unit4Base
class BankAccountInfo.(Unit4Base):


    def get_bankAccountInfo_byOrganizationid_and_indexNumber(self, database, organizationId, indexNumber, ):
        request_args = locals()
        url_template = 'api/{database}/BankAccountInfo/{organizationId}/{indexNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    