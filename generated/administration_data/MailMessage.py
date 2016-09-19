import requests, json
from generated.base.unit4_base import Unit4Base
class MailMessage(Unit4Base):


    def delete_mailMessage_byId(self, database, id, ):
        request_args = locals()
        url_template = 'api/{database}/MailMessage/{id}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_mailMessage_byId(self, database, id, ):
        request_args = locals()
        url_template = 'api/{database}/MailMessage/{id}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_mailMessage(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/MailMessage'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_mailMessage_byId(self, database, id, ):
        request_args = locals()
        url_template = 'api/{database}/MailMessage/{id}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    