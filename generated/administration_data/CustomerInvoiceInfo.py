import requests, json
from generated.base.unit4_base import Unit4Base
class CustomerInvoiceInfo(Unit4Base):


    def get_{fiscalYear}_{invoiceState}_byFiscalyear_and_invoiceState(self, database, fiscalYear, invoiceState, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerInvoiceInfoList/ByFiscalYear/{fiscalYear}/{invoiceState}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{fiscalYear}_{invoiceState}_byFiscalyear_and_invoiceState_and_fiscalYear_and_invoiceState_and_id(self, database, fiscalYear, invoiceState, id, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerInvoiceInfoList/ByFiscalYear/{fiscalYear}/{invoiceState}?id={id}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{fiscalYear}_{id}_byFiscalyear_and_id_and_fiscalYear_and_id_and_invoiceState(self, database, fiscalYear, id, invoiceState, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerInvoiceInfoList/ByFiscalYear/{fiscalYear}/{id}?invoiceState={invoiceState}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{fiscalYear}_{id}_byFiscalyear_and_id(self, database, fiscalYear, id, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerInvoiceInfoList/ByFiscalYear/{fiscalYear}/{id}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_customerInvoiceInfoList_byId(self, database, id, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerInvoiceInfoList/OpenInvoices/{id}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{startDate}_{endDate}_byId_and_startDate_and_Id_and_startDate_and_endDate_and_invoiceState(self, database, Id, startDate, endDate, invoiceState, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerInvoiceInfoList/{Id}/{startDate}/{endDate}?invoiceState={invoiceState}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_customerInvoiceInfoList_byId_and_invoiceState_and_id_and_invoiceState_and_startDate_and_endDate(self, database, id, invoiceState, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerInvoiceInfoList/{id}/{invoiceState}?startDate={startDate}&amp;endDate={endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_customerInvoiceInfoList_byId_and_startDate_and_id_and_startDate_and_endDate(self, database, id, startDate, endDate, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerInvoiceInfoList/{id}?startDate={startDate}&amp;endDate={endDate}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_customerInvoiceInfoList_byId_and_invoiceState(self, database, Id, invoiceState, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerInvoiceInfoList/{Id}?invoiceState={invoiceState}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_customerInvoiceInfoList_byId(self, database, Id, ):
        request_args = locals()
        url_template = 'api/{database}/CustomerInvoiceInfoList/{Id}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    