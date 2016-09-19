import requests, json
from generated.base.unit4_base import Unit4Base
class ProductGroup(Unit4Base):


    def delete_productGroup_byProductgroupid(self, database, productGroupId, ):
        request_args = locals()
        url_template = 'api/{database}/ProductGroup/{productGroupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_productGroup_byProductgroupid(self, database, productGroupId, ):
        request_args = locals()
        url_template = 'api/{database}/ProductGroup/{productGroupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_productGroup(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/ProductGroup'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_productGroup_byProductgroupid(self, database, productGroupId, ):
        request_args = locals()
        url_template = 'api/{database}/ProductGroup/{productGroupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    