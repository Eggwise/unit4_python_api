import requests, json
from generated.base.unit4_base import Unit4Base
class SupplierGroupInfo.(Unit4Base):


    def get_supplierGroupInfo_bySuppliergroupid_and_fiscalYear(self, database, supplierGroupId, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/SupplierGroupInfo/{supplierGroupId}?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_supplierGroupInfo_bySuppliergroupid(self, database, supplierGroupId, ):
        request_args = locals()
        url_template = 'api/{database}/SupplierGroupInfo/{supplierGroupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    