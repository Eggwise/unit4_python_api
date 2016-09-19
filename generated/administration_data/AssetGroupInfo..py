import requests, json
from generated.base.unit4_base import Unit4Base
class AssetGroupInfo.(Unit4Base):


    def get_assetGroupInfo_byAssetgroupid_and_fiscalYear(self, database, assetGroupId, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/AssetGroupInfo/{assetGroupId}?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_assetGroupInfo_byAssetgroupid(self, database, assetGroupId, ):
        request_args = locals()
        url_template = 'api/{database}/AssetGroupInfo/{assetGroupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    