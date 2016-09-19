import requests, json
from generated.base.unit4_base import Unit4Base
class DueSupplierInvoiceStatistics.(Unit4Base):


    def get_dueSupplierInvoiceStatistics_byReferencedate(self, database, referenceDate, ):
        request_args = locals()
        url_template = 'api/{database}/DueSupplierInvoiceStatistics/ByDate/{referenceDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_dueSupplierInvoiceStatistics_byEnityid(self, database, enityId, ):
        request_args = locals()
        url_template = 'api/{database}/DueSupplierInvoiceStatistics?enityId={enityId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_dueSupplierInvoiceStatistics(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/DueSupplierInvoiceStatistics'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    