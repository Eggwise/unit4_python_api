import requests, json
from generated.base.unit4_base import Unit4Base
class Mandate(Unit4Base):


    def delete_mandate_byMandateid(self, database, mandateId, ):
        request_args = locals()
        url_template = 'api/{database}/Mandate/{mandateId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_mandate_byMandateid(self, database, mandateId, ):
        request_args = locals()
        url_template = 'api/{database}/Mandate/{mandateId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_mandate(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Mandate'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_mandate_byMandateid(self, database, mandateId, ):
        request_args = locals()
        url_template = 'api/{database}/Mandate/{mandateId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    