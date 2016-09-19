import requests, json
from generated.base.unit4_base import Unit4Base
class QuoteInfo.(Unit4Base):


    def get_quoteInfo_byQuoteid(self, database, quoteId, ):
        request_args = locals()
        url_template = 'api/{database}/QuoteInfo/{quoteId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    