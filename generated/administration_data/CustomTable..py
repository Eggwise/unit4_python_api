import requests, json
from generated.base.unit4_base import Unit4Base
class CustomTable.(Unit4Base):


    def get_customTable_byTablename(self, database, tableName, ):
        request_args = locals()
        url_template = 'api/{database}/CustomTable/{tableName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_customTable_byTablename(self, database, tableName, ):
        request_args = locals()
        url_template = 'api/{database}/CustomTable/{tableName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    