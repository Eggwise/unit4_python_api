import requests, json
from generated.base.unit4_base import Unit4Base
class DmDocumentCategory(Unit4Base):


    def get_dmDocumentCategoryList_byLinktype(self, database, linkType, ):
        request_args = locals()
        url_template = 'api/{database}/DmDocumentCategoryList?linkType={linkType}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_dmDocumentCategoryList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/DmDocumentCategoryList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_dmDocumentCategoryList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/DmDocumentCategoryList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    