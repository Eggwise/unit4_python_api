import requests, json
from generated.base.unit4_base import Unit4Base
class ProjectInfo.(Unit4Base):


    def get_projectInfo_byProjectid(self, database, projectId, ):
        request_args = locals()
        url_template = 'api/{database}/ProjectInfo/{projectId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    