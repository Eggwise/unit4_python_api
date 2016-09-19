import requests, json
from generated.base.unit4_base import Unit4Base
class DueCustomerInvoiceStatistics.(Unit4Base):


    def get_dueCustomerInvoiceStatistics_byReferencedate(self, database, referenceDate, ):
        request_args = locals()
        url_template = 'api/{database}/DueCustomerInvoiceStatistics/ByDate/{referenceDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_dueCustomerInvoiceStatistics_byEnityid(self, database, enityId, ):
        request_args = locals()
        url_template = 'api/{database}/DueCustomerInvoiceStatistics?enityId={enityId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_dueCustomerInvoiceStatistics(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/DueCustomerInvoiceStatistics'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    