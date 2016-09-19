import requests, json
from generated.base.unit4_base import Unit4Base
class PurchaseInfo.(Unit4Base):


    def get_purchaseInfo_byProductid_and_sequenceNumber(self, database, productId, sequenceNumber, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseInfo/{productId}/{sequenceNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    