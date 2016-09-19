import requests, json
from generated.base.unit4_base import Unit4Base
class CustomFieldDefinitionInfo(Unit4Base):


    def get_customFieldDefinitionInfoList_byEntities(self, database, entities, ):
        request_args = locals()
        url_template = 'api/{database}/CustomFieldDefinitionInfoList/{entities}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    