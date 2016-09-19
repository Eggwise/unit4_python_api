import requests, json
from generated.base.unit4_base import Unit4Base
class SpecPrice(Unit4Base):


    def delete_specPrice_bySpecpriceid(self, database, specPriceId, ):
        request_args = locals()
        url_template = 'api/{database}/SpecPrice/{specPriceId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_specPrice_bySpecpriceid(self, database, specPriceId, ):
        request_args = locals()
        url_template = 'api/{database}/SpecPrice/{specPriceId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_specPrice(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/SpecPrice'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_specPrice_bySpecpriceid(self, database, specPriceId, ):
        request_args = locals()
        url_template = 'api/{database}/SpecPrice/{specPriceId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    