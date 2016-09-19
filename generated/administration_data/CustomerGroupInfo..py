import requests, json
from generated.base.unit4_base import Unit4Base
class CustomerGroupInfo.(Unit4Base):


    def get_customerGroupInfo_byCustomergroupid_and_fiscalYear(self, database, customerGroupId, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerGroupInfo/{customerGroupId}?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_customerGroupInfo_byCustomergroupid(self, database, customerGroupId, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerGroupInfo/{customerGroupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    