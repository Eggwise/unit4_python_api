import requests, json
from generated.base.unit4_base import Unit4Base
class KeyPerformanceIndicatorLine.(Unit4Base):


    def get_keyPerformanceIndicatorLine_byFiscalyear_and_statementId(self, database, fiscalYear, statementId, ):
        request_args = locals()
        url_template = 'api/{database}/KeyPerformanceIndicatorLine/{fiscalYear}/{statementId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    