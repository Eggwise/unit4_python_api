import requests, json
from generated.base.unit4_base import Unit4Base
class Task(Unit4Base):


    def get_taskList_byOrganizationid_and_customerId_and_organizationId_and_customerId_and_supplierId(self, database, organizationId, customerId, supplierId, ):
        request_args = locals()
        url_template = 'api/{database}/TaskList/{organizationId}?customerId={customerId}&amp;supplierId={supplierId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_taskList_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/TaskList/{organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_taskList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/TaskList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    