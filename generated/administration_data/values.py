import requests, json
from generated.base.unit4_base import Unit4Base
class values(Unit4Base):


    def create_payable(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Payable'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    