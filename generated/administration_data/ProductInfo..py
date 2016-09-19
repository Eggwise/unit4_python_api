import requests, json
from generated.base.unit4_base import Unit4Base
class ProductInfo.(Unit4Base):


    def get_productInfo_byProductid(self, database, productId, ):
        request_args = locals()
        url_template = 'api/{database}/ProductInfo/{productId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    