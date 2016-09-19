import requests, json
from generated.base.unit4_base import Unit4Base
class BankInfo.(Unit4Base):


    def get_bankInfo_byBankid(self, database, bankId, ):
        request_args = locals()
        url_template = 'api/{database}/BankInfo/{bankId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    