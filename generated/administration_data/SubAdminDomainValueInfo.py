import requests, json
from generated.base.unit4_base import Unit4Base
class SubAdminDomainValueInfo(Unit4Base):


    def get_subAdminDomainValueInfoList_byDomainid(self, database, domainId, ):
        request_args = locals()
        url_template = 'api/{database}/SubAdminDomainValueInfoList/{domainId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    