import requests, json
from generated.base.unit4_base import Unit4Base
class CostUnit(Unit4Base):


    def delete_costUnit_byCostunitid(self, database, costUnitId, ):
        request_args = locals()
        url_template = 'api/{database}/CostUnit/{costUnitId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_costUnit_byCostunitid(self, database, costUnitId, ):
        request_args = locals()
        url_template = 'api/{database}/CostUnit/{costUnitId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_costUnit(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/CostUnit'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_costUnit_byCostunitid(self, database, costUnitId, ):
        request_args = locals()
        url_template = 'api/{database}/CostUnit/{costUnitId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    