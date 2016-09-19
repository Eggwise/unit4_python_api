import requests, json
from generated.base.unit4_base import Unit4Base
class CostCentre(Unit4Base):


    def delete_costCentre_byCostcentreid(self, database, costCentreId, ):
        request_args = locals()
        url_template = 'api/{database}/CostCentre/{costCentreId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_costCentre_byCostcentreid(self, database, costCentreId, ):
        request_args = locals()
        url_template = 'api/{database}/CostCentre/{costCentreId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_costCentre(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/CostCentre'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_costCentre_byCostcentreid(self, database, costCentreId, ):
        request_args = locals()
        url_template = 'api/{database}/CostCentre/{costCentreId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    