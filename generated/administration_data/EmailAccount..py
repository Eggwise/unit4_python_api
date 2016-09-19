import requests, json
from generated.base.unit4_base import Unit4Base
class EmailAccount.(Unit4Base):


    def get_emailAccount(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/EmailAccount'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_emailAccount(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/EmailAccount'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_emailAccount(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/EmailAccount'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    