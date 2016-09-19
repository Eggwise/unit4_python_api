import requests, json
from generated.base.unit4_base import Unit4Base
class Organization(Unit4Base):


    def delete_organization_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/Organization/{organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_organization_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/Organization/{organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_organization(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Organization'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_organization_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/Organization/{organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    