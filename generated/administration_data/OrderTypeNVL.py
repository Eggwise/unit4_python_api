import requests, json
from generated.base.unit4_base import Unit4Base
class OrderTypeNVL(Unit4Base):


    def get_orderTypeNVL(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/OrderTypeNVL'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    