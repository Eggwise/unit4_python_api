import requests, json
from generated.base.unit4_base import Unit4Base
class OrganizationDocumentsOutput(Unit4Base):


    def delete_organizationDocumentsOutput_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/OrganizationDocumentsOutput/{organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_organizationDocumentsOutput_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/OrganizationDocumentsOutput/{organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_organizationDocumentsOutput_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/OrganizationDocumentsOutput/{organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    