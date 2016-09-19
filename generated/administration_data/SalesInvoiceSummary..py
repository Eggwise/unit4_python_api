import requests, json
from generated.base.unit4_base import Unit4Base
class SalesInvoiceSummary.(Unit4Base):


    def get_salesInvoiceSummary_byCustomerid_and_fiscalYear_and_customerId_and_fiscalYear_and_startDate(self, database, customerId, fiscalYear, startDate, ):
        request_args = locals()
        url_template = 'api/{database}/SalesInvoiceSummary/{customerId}/{fiscalYear}?startDate={startDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesInvoiceSummary_byCustomerid_and_startDate_and_customerId_and_startDate_and_endDate_and_fiscalYear(self, database, customerId, startDate, endDate, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/SalesInvoiceSummary/{customerId}/{startDate}?endDate={endDate}&amp;fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesInvoiceSummary_byCustomerid_and_startDate_and_customerId_and_startDate_and_endDate(self, database, customerId, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/SalesInvoiceSummary/{customerId}/{startDate}?endDate={endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesInvoiceSummary_byCustomerid_and_startDate_and_customerId_and_startDate_and_fiscalYear(self, database, customerId, startDate, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/SalesInvoiceSummary/{customerId}/{startDate}?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesInvoiceSummary_byCustomerid_and_startDate_and_customerId_and_startDate_and_endDate_and_fiscalYear(self, database, customerId, startDate, endDate, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/SalesInvoiceSummary/{customerId}?startDate={startDate}&amp;endDate={endDate}&amp;fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesInvoiceSummary_byCustomerid_and_startDate_and_customerId_and_startDate_and_endDate(self, database, customerId, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/SalesInvoiceSummary/{customerId}?startDate={startDate}&amp;endDate={endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesInvoiceSummary_byCustomerid_and_fiscalYear(self, database, customerId, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/SalesInvoiceSummary/{customerId}?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesInvoiceSummary_byCustomerid_and_startDate(self, database, customerId, startDate, ):
        request_args = locals()
        url_template = 'api/{database}/SalesInvoiceSummary/{customerId}?startDate={startDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_salesInvoiceSummary_byCustomerid(self, database, customerId, ):
        request_args = locals()
        url_template = 'api/{database}/SalesInvoiceSummary/{customerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    