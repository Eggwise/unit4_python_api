import requests, json
from generated.base.unit4_base import Unit4Base
class DocumentTypeInfo(Unit4Base):


    def get_documentTypeInfoList_byMailtemplatesafe(self, database, mailTemplateSafe, ):
        request_args = locals()
        url_template = 'api/{database}/DocumentTypeInfoList?mailTemplateSafe={mailTemplateSafe}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_documentTypeInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/DocumentTypeInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    