import requests, json
from generated.base.unit4_base import Unit4Base
class PurchaseInfo(Unit4Base):


    def get_purchaseInfoList_bySupplierid_and_productId(self, database, supplierId, productId, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseInfoList?supplierId={supplierId}&amp;productId={productId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_purchaseInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    