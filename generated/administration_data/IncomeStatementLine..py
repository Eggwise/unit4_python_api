import requests, json
from generated.base.unit4_base import Unit4Base
class IncomeStatementLine.(Unit4Base):


    def get_{fiscalYear}_{statementId}_byFiscalyear_and_statementId(self, database, fiscalYear, statementId, ):
        request_args = locals()
        url_template = 'api/{database}/IncomeStatementLine/WithBreakdown/{fiscalYear}/{statementId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_incomeStatementLine_byFiscalyear_and_statementId(self, database, fiscalYear, statementId, ):
        request_args = locals()
        url_template = 'api/{database}/IncomeStatementLine/{fiscalYear}/{statementId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    