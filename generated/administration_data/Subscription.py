import requests, json
from generated.base.unit4_base import Unit4Base
class Subscription(Unit4Base):


    def delete_subscription_bySubscriptionid(self, database, subscriptionId, ):
        request_args = locals()
        url_template = 'api/{database}/Subscription/{subscriptionId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_subscription_bySubscriptionid(self, database, subscriptionId, ):
        request_args = locals()
        url_template = 'api/{database}/Subscription/{subscriptionId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_subscription(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Subscription'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_subscription_bySubscriptionid(self, database, subscriptionId, ):
        request_args = locals()
        url_template = 'api/{database}/Subscription/{subscriptionId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    