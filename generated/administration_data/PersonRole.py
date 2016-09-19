import requests, json
from generated.base.unit4_base import Unit4Base
class PersonRole(Unit4Base):


    def get_personRoleList_byPersonid(self, database, personId, ):
        request_args = locals()
        url_template = 'api/{database}/PersonRoleList?personId={personId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_personRoleList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/PersonRoleList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_personRoleList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/PersonRoleList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    