import requests, json
from generated.base.unit4_base import Unit4Base
class AccountManager(Unit4Base):


    def delete_accountManager_byAccountmanagerid(self, database, accountManagerId, ):
        request_args = locals()
        url_template = 'api/{database}/AccountManager/{accountManagerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_accountManager_byAccountmanagerid(self, database, accountManagerId, ):
        request_args = locals()
        url_template = 'api/{database}/AccountManager/{accountManagerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_accountManager(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/AccountManager'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_accountManager_byAccountmanagerid(self, database, accountManagerId, ):
        request_args = locals()
        url_template = 'api/{database}/AccountManager/{accountManagerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    