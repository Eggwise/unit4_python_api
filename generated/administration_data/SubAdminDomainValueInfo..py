import requests, json
from generated.base.unit4_base import Unit4Base
class SubAdminDomainValueInfo.(Unit4Base):


    def get_subAdminDomainValueInfo_byDomainid_and_domainValueId(self, database, domainId, domainValueId, ):
        request_args = locals()
        url_template = 'api/{database}/SubAdminDomainValueInfo/{domainId}/{domainValueId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    