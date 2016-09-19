import requests, json
from generated.base.unit4_base import Unit4Base
class SupplierInvoiceStatistics.(Unit4Base):


    def get_supplierInvoiceStatistics_bySupplierid_and_referenceDate(self, database, supplierId, referenceDate, ):
        request_args = locals()
        url_template = 'api/{database}/SupplierInvoiceStatistics/{supplierId}?referenceDate={referenceDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_supplierInvoiceStatistics_bySupplierid(self, database, supplierId, ):
        request_args = locals()
        url_template = 'api/{database}/SupplierInvoiceStatistics/{supplierId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    