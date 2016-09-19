import requests, json
from generated.base.unit4_base import Unit4Base
class ContactInfo(Unit4Base):


    def get_contactInfoList_byEmail_and_name(self, database, email, name, ):
        request_args = locals()
        url_template = 'api/{database}/ContactInfoList/{email}/{name}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_contactInfoList_byEmail_and_name_and_email_and_name_and_organizationId(self, database, email, name, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/ContactInfoList/{email}/{name}?organizationId={organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_contactInfoList_byOrganizationid_and_email_and_organizationId_and_email_and_name(self, database, organizationId, email, name, ):
        request_args = locals()
        url_template = 'api/{database}/ContactInfoList/{organizationId}?email={email}&amp;name={name}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_contactInfoList_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/ContactInfoList/{organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    