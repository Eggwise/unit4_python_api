import requests, json
from generated.base.unit4_base import Unit4Base
class AddressInfo.(Unit4Base):


    def get_addressInfo_byAddressguid(self, database, addressGuid, ):
        request_args = locals()
        url_template = 'api/{database}/AddressInfo/{addressGuid}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    