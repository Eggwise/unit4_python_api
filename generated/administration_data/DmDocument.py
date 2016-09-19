import requests, json
from generated.base.unit4_base import Unit4Base
class DmDocument(Unit4Base):


    def get_dmDocumentList_byLinktype(self, database, linkType, ):
        request_args = locals()
        url_template = 'api/{database}/DmDocumentList/ByLinkType/{linkType}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_dmDocumentList_byOrganizationid(self, database, organizationId, ):
        request_args = locals()
        url_template = 'api/{database}/DmDocumentList/ByOrganization/{organizationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_dmDocumentList_byPattern(self, database, pattern, ):
        request_args = locals()
        url_template = 'api/{database}/DmDocumentList/ByPattern/{pattern}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_dmDocumentList_byLinktype_and_linkValue_and_linkType_and_linkValue_and_pattern(self, database, linkType, linkValue, pattern, ):
        request_args = locals()
        url_template = 'api/{database}/DmDocumentList/{linkType}/{linkValue}?pattern={pattern}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_dmDocumentList_byLinktype_and_linkValue_and_linkType_and_linkValue_and_pattern(self, database, linkType, linkValue, pattern, ):
        request_args = locals()
        url_template = 'api/{database}/DmDocumentList?linkType={linkType}&amp;linkValue={linkValue}&amp;pattern={pattern}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_dmDocumentList_byLinktype_and_linkValue(self, database, linkType, linkValue, ):
        request_args = locals()
        url_template = 'api/{database}/DmDocumentList?linkType={linkType}&amp;linkValue={linkValue}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_dmDocumentList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/DmDocumentList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    