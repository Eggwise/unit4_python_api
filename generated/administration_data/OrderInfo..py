import requests, json
from generated.base.unit4_base import Unit4Base
class OrderInfo.(Unit4Base):


    def get_orderInfo_byInvoiceid(self, database, invoiceId, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfo/ByInvoiceId/{invoiceId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_orderInfo(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfo/SampleData'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_orderInfo_byOrderid(self, database, orderId, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfo/{orderId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    