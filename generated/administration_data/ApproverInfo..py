import requests, json
from generated.base.unit4_base import Unit4Base
class ApproverInfo.(Unit4Base):


    def get_approverInfo_byEntity_and_approverId(self, database, entity, approverId, ):
        request_args = locals()
        url_template = 'api/{database}/ApproverInfo/{entity}?approverId={approverId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_approverInfo_byEntity(self, database, entity, ):
        request_args = locals()
        url_template = 'api/{database}/ApproverInfo/{entity}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    