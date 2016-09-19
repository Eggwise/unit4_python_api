import requests, json
from generated.base.unit4_base import Unit4Base
class VatScenarioRuleInfo(Unit4Base):


    def get_vatScenarioRuleInfoList_byFiscalyear_and_scenarioId(self, database, fiscalYear, scenarioId, ):
        request_args = locals()
        url_template = 'api/{database}/VatScenarioRuleInfoList/{fiscalYear}?scenarioId={scenarioId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_vatScenarioRuleInfoList_byFiscalyear_and_scenarioId(self, database, fiscalYear, scenarioId, ):
        request_args = locals()
        url_template = 'api/{database}/VatScenarioRuleInfoList?fiscalYear={fiscalYear}&amp;scenarioId={scenarioId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_vatScenarioRuleInfoList_byFiscalyear(self, database, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/VatScenarioRuleInfoList?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_vatScenarioRuleInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/VatScenarioRuleInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    