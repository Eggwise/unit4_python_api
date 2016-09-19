import requests, json
from generated.base.unit4_base import Unit4Base
class ProjectProductNVL(Unit4Base):


    def get_projectProductNVL_byProjectentrytype(self, database, projectEntryType, ):
        request_args = locals()
        url_template = 'api/{database}/ProjectProductNVL/{projectEntryType}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    