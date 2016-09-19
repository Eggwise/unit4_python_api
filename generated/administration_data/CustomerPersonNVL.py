import requests, json
from generated.base.unit4_base import Unit4Base
class CustomerPersonNVL(Unit4Base):


    def get_customerPersonNVL_byCustomerid(self, database, customerId, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerPersonNVL/{customerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    