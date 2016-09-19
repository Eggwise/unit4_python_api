import requests, json
from generated.base.unit4_base import Unit4Base
class RoleNVL(Unit4Base):


    def get_roleNVL_byPersonroletype(self, database, personRoleType, ):
        request_args = locals()
        url_template = 'api/{database}/RoleNVL?personRoleType={personRoleType}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_roleNVL(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/RoleNVL'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    