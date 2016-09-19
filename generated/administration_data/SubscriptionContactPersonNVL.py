import requests, json
from generated.base.unit4_base import Unit4Base
class SubscriptionContactPersonNVL(Unit4Base):


    def get_subscriptionContactPersonNVL_byCustomerid(self, database, customerId, ):
        request_args = locals()
        url_template = 'api/{database}/SubscriptionContactPersonNVL/{customerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    