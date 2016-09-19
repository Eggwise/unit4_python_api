import requests, json
from generated.base.unit4_base import Unit4Base
class OrganizationNVL(Unit4Base):


    def get_organizationNVL_byMustbecustomer_and_mustBeSupplier(self, database, mustBeCustomer, mustBeSupplier, ):
        request_args = locals()
        url_template = 'api/{database}/OrganizationNVL?mustBeCustomer={mustBeCustomer}&amp;mustBeSupplier={mustBeSupplier}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_organizationNVL(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/OrganizationNVL'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    