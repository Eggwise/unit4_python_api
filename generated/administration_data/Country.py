import requests, json
from generated.base.unit4_base import Unit4Base
class Country(Unit4Base):


    def delete_country_byCountryid(self, database, countryId, ):
        request_args = locals()
        url_template = 'api/{database}/Country/{countryId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_country_byCountryid(self, database, countryId, ):
        request_args = locals()
        url_template = 'api/{database}/Country/{countryId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_country(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Country'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_country_byCountryid(self, database, countryId, ):
        request_args = locals()
        url_template = 'api/{database}/Country/{countryId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    