import requests, json
from generated.base.unit4_base import Unit4Base
class OrganizationInfo(Unit4Base):


    def get_organizationInfoList_byEmail_and_shortName_and_email_and_shortName_and_name_and_city(self, database, email, shortName, name, city, ):
        request_args = locals()
        url_template = 'api/{database}/OrganizationInfoList?email={email}&amp;shortName={shortName}&amp;name={name}&amp;city={city}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_organizationInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/OrganizationInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    