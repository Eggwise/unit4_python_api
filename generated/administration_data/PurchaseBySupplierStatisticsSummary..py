import requests, json
from generated.base.unit4_base import Unit4Base
class PurchaseBySupplierStatisticsSummary.(Unit4Base):


    def get_{fiscalyear}_{startPeriod}_byFiscalyear_and_startPeriod_and_fiscalyear_and_startPeriod_and_endPeriod(self, database, fiscalyear, startPeriod, endPeriod, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForInvoicesInPeriod/{fiscalyear}/{startPeriod}/{endPeriod}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate(self, database, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForInvoices/{startDate}/{endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate_and_startDate_and_endDate_and_fiscalyear(self, database, startDate, endDate, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForInvoices/{startDate}/{endDate}?fiscalyear={fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_purchaseBySupplierStatisticsSummary_byFiscalyear_and_startDate_and_fiscalyear_and_startDate_and_endDate(self, database, fiscalyear, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForInvoices/{fiscalyear}?startDate={startDate}&amp;endDate={endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_purchaseBySupplierStatisticsSummary_byFiscalyear(self, database, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForInvoices/{fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate(self, database, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForOrdersIncludingNotYetInvoiced/{startDate}/{endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate_and_startDate_and_endDate_and_fiscalyear(self, database, startDate, endDate, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForOrdersIncludingNotYetInvoiced/{startDate}/{endDate}?fiscalyear={fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_purchaseBySupplierStatisticsSummary_byFiscalyear_and_startDate_and_fiscalyear_and_startDate_and_endDate(self, database, fiscalyear, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForOrdersIncludingNotYetInvoiced/{fiscalyear}?startDate={startDate}&amp;endDate={endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_purchaseBySupplierStatisticsSummary_byFiscalyear(self, database, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForOrdersIncludingNotYetInvoiced/{fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate(self, database, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForOrders/{startDate}/{endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate_and_startDate_and_endDate_and_fiscalyear(self, database, startDate, endDate, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForOrders/{startDate}/{endDate}?fiscalyear={fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_purchaseBySupplierStatisticsSummary_byFiscalyear_and_startDate_and_fiscalyear_and_startDate_and_endDate(self, database, fiscalyear, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForOrders/{fiscalyear}?startDate={startDate}&amp;endDate={endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_purchaseBySupplierStatisticsSummary_byFiscalyear(self, database, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/PurchaseBySupplierStatisticsSummary/ForOrders/{fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    