import requests, json
from generated.base.unit4_base import Unit4Base
class AssetInfo.(Unit4Base):


    def get_assetInfo_byAssetid_and_fiscalYear(self, database, assetId, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/AssetInfo/{assetId}?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_assetInfo_byAssetid(self, database, assetId, ):
        request_args = locals()
        url_template = 'api/{database}/AssetInfo/{assetId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    