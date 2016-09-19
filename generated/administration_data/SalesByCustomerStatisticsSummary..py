import requests, json
from generated.base.unit4_base import Unit4Base
class SalesByCustomerStatisticsSummary.(Unit4Base):


    def get_{fiscalyear}_{startPeriod}_byFiscalyear_and_startPeriod_and_fiscalyear_and_startPeriod_and_endPeriod(self, database, fiscalyear, startPeriod, endPeriod, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForInvoicesInPeriod/{fiscalyear}/{startPeriod}/{endPeriod}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate(self, database, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForInvoices/{startDate}/{endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate_and_startDate_and_endDate_and_fiscalyear(self, database, startDate, endDate, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForInvoices/{startDate}/{endDate}?fiscalyear={fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesByCustomerStatisticsSummary_byFiscalyear_and_startDate_and_fiscalyear_and_startDate_and_endDate(self, database, fiscalyear, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForInvoices/{fiscalyear}?startDate={startDate}&amp;endDate={endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesByCustomerStatisticsSummary_byFiscalyear(self, database, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForInvoices/{fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate(self, database, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForOrdersIncludingNotYetInvoiced/{startDate}/{endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate_and_startDate_and_endDate_and_fiscalyear(self, database, startDate, endDate, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForOrdersIncludingNotYetInvoiced/{startDate}/{endDate}?fiscalyear={fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesByCustomerStatisticsSummary_byFiscalyear_and_startDate_and_fiscalyear_and_startDate_and_endDate(self, database, fiscalyear, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForOrdersIncludingNotYetInvoiced/{fiscalyear}?startDate={startDate}&amp;endDate={endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesByCustomerStatisticsSummary_byFiscalyear(self, database, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForOrdersIncludingNotYetInvoiced/{fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate(self, database, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForOrders/{startDate}/{endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byStartdate_and_endDate_and_startDate_and_endDate_and_fiscalyear(self, database, startDate, endDate, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForOrders/{startDate}/{endDate}?fiscalyear={fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesByCustomerStatisticsSummary_byFiscalyear_and_startDate_and_fiscalyear_and_startDate_and_endDate(self, database, fiscalyear, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForOrders/{fiscalyear}?startDate={startDate}&amp;endDate={endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesByCustomerStatisticsSummary_byFiscalyear(self, database, fiscalyear, ):
        request_args = locals()
        url_template = 'api/{database}/SalesByCustomerStatisticsSummary/ForOrders/{fiscalyear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    