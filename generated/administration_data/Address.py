import requests, json
from generated.base.unit4_base import Unit4Base
class Address(Unit4Base):


    def get_addressList_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/AddressList/{organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_addressList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/AddressList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    