import requests, json
from generated.base.unit4_base import Unit4Base
class QuoteInfo(Unit4Base):


    def get_quoteInfoList_byOrgid(self, database, orgId, ):
        request_args = locals()
        url_template = 'api/{database}/QuoteInfoList/OpenQuotes/{orgId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_quoteInfoList_byOrgid(self, database, orgId, ):
        request_args = locals()
        url_template = 'api/{database}/QuoteInfoList/{orgId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    