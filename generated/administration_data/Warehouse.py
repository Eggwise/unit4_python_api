import requests, json
from generated.base.unit4_base import Unit4Base
class Warehouse(Unit4Base):


    def delete_warehouse_byWarehouseid(self, database, warehouseId, ):
        request_args = locals()
        url_template = 'api/{database}/Warehouse/{warehouseId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_warehouse(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Warehouse/Preferred'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_warehouse_byWarehouseid(self, database, warehouseId, ):
        request_args = locals()
        url_template = 'api/{database}/Warehouse/{warehouseId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_warehouse(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Warehouse'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_warehouse_byWarehouseid(self, database, warehouseId, ):
        request_args = locals()
        url_template = 'api/{database}/Warehouse/{warehouseId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    