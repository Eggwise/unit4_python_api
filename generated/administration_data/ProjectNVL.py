import requests, json
from generated.base.unit4_base import Unit4Base
class ProjectNVL(Unit4Base):


    def get_projectNVL(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/ProjectNVL'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    