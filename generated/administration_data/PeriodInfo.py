import requests, json
from generated.base.unit4_base import Unit4Base
class PeriodInfo(Unit4Base):


    def get_periodInfoList_byFiscalyear(self, database, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/PeriodInfoList?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_periodInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/PeriodInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    