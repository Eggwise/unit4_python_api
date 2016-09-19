import requests, json
from generated.base.unit4_base import Unit4Base
class ContactInfo.(Unit4Base):


    def get_contactInfo_byOrganizationid_and_contactId(self, database, organizationId, contactId, ):
        request_args = locals()
        url_template = 'api/{database}/ContactInfo/{organizationId}/{contactId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    