import requests, json
from generated.base.unit4_base import Unit4Base
class HourTypeInfo(Unit4Base):


    def get_hourTypeInfoList_byDescription_and_hourCategory_and_description_and_hourCategory_and_hourGroupId_and_searchName_and_status_and_hourTypeId(self, database, description, hourCategory, hourGroupId, searchName, status, hourTypeId, ):
        request_args = locals()
        url_template = 'api/{database}/HourTypeInfoList?description={description}&amp;hourCategory={hourCategory}&amp;hourGroupId={hourGroupId}&amp;searchName={searchName}&amp;status={status}&amp;hourTypeId={hourTypeId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_hourTypeInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/HourTypeInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    