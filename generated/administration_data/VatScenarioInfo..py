import requests, json
from generated.base.unit4_base import Unit4Base
class VatScenarioInfo.(Unit4Base):


    def get_vatScenarioInfo_byScenarioid_and_fiscalYear(self, database, scenarioId, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/VatScenarioInfo/{scenarioId}/{fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    