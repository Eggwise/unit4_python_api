import requests, json
from generated.base.unit4_base import Unit4Base
class Person(Unit4Base):


    def delete_person_byPersonid(self, database, personId, ):
        request_args = locals()
        url_template = 'api/{database}/Person/{personId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_person_byPersonid(self, database, personId, ):
        request_args = locals()
        url_template = 'api/{database}/Person/{personId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_person(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Person'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_person_byPersonid(self, database, personId, ):
        request_args = locals()
        url_template = 'api/{database}/Person/{personId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    