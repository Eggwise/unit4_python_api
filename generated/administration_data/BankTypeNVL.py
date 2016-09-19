import requests, json
from generated.base.unit4_base import Unit4Base
class BankTypeNVL(Unit4Base):


    def get_bankTypeNVL(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/BankTypeNVL'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    