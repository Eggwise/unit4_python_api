import requests, json
from generated.base.unit4_base import Unit4Base
class Currency(Unit4Base):


    def delete_currency_byCurrencyid(self, database, currencyId, ):
        request_args = locals()
        url_template = 'api/{database}/Currency/{currencyId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_currency_byCurrencyid(self, database, currencyId, ):
        request_args = locals()
        url_template = 'api/{database}/Currency/{currencyId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_currency(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Currency'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_currency_byCurrencyid(self, database, currencyId, ):
        request_args = locals()
        url_template = 'api/{database}/Currency/{currencyId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    