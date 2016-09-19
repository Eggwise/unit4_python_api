import requests, json
from generated.base.unit4_base import Unit4Base
class BankAccount(Unit4Base):


    def get_bankAccountList_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/BankAccountList/{organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_bankAccountList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/BankAccountList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    