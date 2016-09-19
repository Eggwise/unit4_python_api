import requests, json
from generated.base.unit4_base import Unit4Base
class SupplierInvoice(Unit4Base):


    def delete_supplierInvoice_byInvoiceid(self, database, invoiceId, ):
        request_args = locals()
        url_template = 'api/{database}/SupplierInvoice/{invoiceId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_supplierInvoice_byInvoiceid(self, database, invoiceId, ):
        request_args = locals()
        url_template = 'api/{database}/SupplierInvoice/{invoiceId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_supplierInvoice(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/SupplierInvoice'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_supplierInvoice_byInvoiceid(self, database, invoiceId, ):
        request_args = locals()
        url_template = 'api/{database}/SupplierInvoice/{invoiceId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    