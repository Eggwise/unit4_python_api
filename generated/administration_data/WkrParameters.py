import requests, json
from generated.base.unit4_base import Unit4Base
class WkrParameters(Unit4Base):


    def delete_wkrParameters_byCalendaryear(self, database, calendarYear, ):
        request_args = locals()
        url_template = 'api/{database}/WkrParameters/{calendarYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_wkrParameters_byCalendaryear(self, database, calendarYear, ):
        request_args = locals()
        url_template = 'api/{database}/WkrParameters/{calendarYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_wkrParameters(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/WkrParameters'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_wkrParameters_byCalendaryear(self, database, calendarYear, ):
        request_args = locals()
        url_template = 'api/{database}/WkrParameters/{calendarYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    