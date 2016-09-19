import requests, json
from generated.base.unit4_base import Unit4Base
class BankAccountInfo(Unit4Base):


    def get_bankAccountInfoList_byCustomerid(self, database, customerId, ):
        request_args = locals()
        url_template = 'api/{database}/BankAccountInfoList/ByCustomerId/{customerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_bankAccountInfoList_bySupplierid(self, database, supplierId, ):
        request_args = locals()
        url_template = 'api/{database}/BankAccountInfoList/BySupplierId/{supplierId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_bankAccountInfoList_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/BankAccountInfoList?organizationId={organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_bankAccountInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/BankAccountInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    