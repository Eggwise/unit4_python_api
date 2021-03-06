import requests, json
from generated.base.unit4_base import Unit4Base
class PurchaseStatisticsSummary.(Unit4Base):


    def get_{fiscalyear}_{type}_byFiscalyear_and_type_and_fiscalyear_and_type_and_yearToDate(self, database, fiscalyear, type, yearToDate, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseStatisticsSummary/ForInvoices/{fiscalyear}/{type}/{yearToDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{fiscalyear}_{type}_byFiscalyear_and_type_and_fiscalyear_and_type_and_yearToDate(self, database, fiscalyear, type, yearToDate, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseStatisticsSummary/ForOrdersIncludingNotYetInvoiced/{fiscalyear}/{type}/{yearToDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{fiscalyear}_{type}_byFiscalyear_and_type_and_fiscalyear_and_type_and_yearToDate(self, database, fiscalyear, type, yearToDate, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseStatisticsSummary/ForOrders/{fiscalyear}/{type}/{yearToDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    