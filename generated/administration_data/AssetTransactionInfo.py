import requests, json
from generated.base.unit4_base import Unit4Base
class AssetTransactionInfo(Unit4Base):


    def get_{fiscalYear}_{assetId}_byFiscalyear_and_assetId(self, database, fiscalYear, assetId, ):
        request_args = locals()
        url_template = 'api/{database}/AssetTransactionInfoList/ByAssetId/{fiscalYear}/{assetId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{fiscalYear}_{startPeriod}_byFiscalyear_and_startPeriod_and_fiscalYear_and_startPeriod_and_endPeriod_and_assetId(self, database, fiscalYear, startPeriod, endPeriod, assetId, ):
        request_args = locals()
        url_template = 'api/{database}/AssetTransactionInfoList/ByPeriod/{fiscalYear}/{startPeriod}/{endPeriod}?assetId={assetId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{fiscalYear}_{startPeriod}_byFiscalyear_and_startPeriod_and_fiscalYear_and_startPeriod_and_endPeriod(self, database, fiscalYear, startPeriod, endPeriod, ):
        request_args = locals()
        url_template = 'api/{database}/AssetTransactionInfoList/ByPeriod/{fiscalYear}/{startPeriod}/{endPeriod}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_assetTransactionInfoList_byFiscalyear(self, database, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/AssetTransactionInfoList/{fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    