import requests, json
from generated.base.unit4_base import Unit4Base
class GetInvoiceDocumentCommand(Unit4Base):


    def get_byOrderId_{orderId}_byOrderid_and_format(self, database, orderId, format, ):
        request_args = locals()
        url_template = 'api/{database}/Documents/Invoice/ByOrderId/{orderId}?format={format}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_documents_byFormat(self, database, format, ):
        request_args = locals()
        url_template = 'api/{database}/Documents/Invoice/Sample?format={format}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_documents_byInvoiceid_and_format(self, database, invoiceId, format, ):
        request_args = locals()
        url_template = 'api/{database}/Documents/Invoice/{invoiceId}?format={format}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    