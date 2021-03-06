import requests, json
from generated.base.unit4_base import Unit4Base
class KeyPerformanceIndicator.(Unit4Base):


    def get_keyPerformanceIndicator_byFiscalyear_and_periodConfiguration(self, database, fiscalYear, periodConfiguration, ):
        request_args = locals()
        url_template = 'api/{database}/KeyPerformanceIndicator/{fiscalYear}?periodConfiguration={periodConfiguration}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_keyPerformanceIndicator_byFiscalyear_and_periodConfiguration(self, database, fiscalYear, periodConfiguration, ):
        request_args = locals()
        url_template = 'api/{database}/KeyPerformanceIndicator?fiscalYear={fiscalYear}&amp;periodConfiguration={periodConfiguration}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_keyPerformanceIndicator_byFiscalyear(self, database, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/KeyPerformanceIndicator?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_keyPerformanceIndicator(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/KeyPerformanceIndicator'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    