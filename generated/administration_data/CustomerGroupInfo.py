import requests, json
from generated.base.unit4_base import Unit4Base
class CustomerGroupInfo(Unit4Base):


    def get_customerGroupInfoList_byFiscalyear(self, database, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerGroupInfoList?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_customerGroupInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerGroupInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    