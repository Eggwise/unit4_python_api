import requests, json
from generated.base.unit4_base import Unit4Base
class Supplier(Unit4Base):


    def delete_supplier_bySupplierid(self, database, supplierId, ):
        request_args = locals()
        url_template = 'api/{database}/Supplier/SupplierAndOrganization/{supplierId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def delete_supplier_bySupplierid(self, database, supplierId, ):
        request_args = locals()
        url_template = 'api/{database}/Supplier/{supplierId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_supplier_bySupplierid(self, database, supplierId, ):
        request_args = locals()
        url_template = 'api/{database}/Supplier/{supplierId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_supplier(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Supplier'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_supplier_bySupplierid(self, database, supplierId, ):
        request_args = locals()
        url_template = 'api/{database}/Supplier/{supplierId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    