import requests, json
from generated.base.unit4_base import Unit4Base
class ProductInfo(Unit4Base):


    def get_productInfoList_byProductid_and_shortName_and_productId_and_shortName_and_description_and_productGroupId(self, database, productId, shortName, description, productGroupId, ):
        request_args = locals()
        url_template = 'api/{database}/ProductInfoList?productId={productId}&amp;shortName={shortName}&amp;description={description}&amp;productGroupId={productGroupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_productInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/ProductInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    