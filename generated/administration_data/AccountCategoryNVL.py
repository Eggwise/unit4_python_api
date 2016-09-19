import requests, json
from generated.base.unit4_base import Unit4Base
class AccountCategoryNVL(Unit4Base):


    def get_accountCategoryNVL_byCategoryid_and_canBeLinkedToAccount(self, database, categoryId, canBeLinkedToAccount, ):
        request_args = locals()
        url_template = 'api/{database}/AccountCategoryNVL/{categoryId}?canBeLinkedToAccount={canBeLinkedToAccount}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_accountCategoryNVL_byCategoryid_and_canBeLinkedToAccount(self, database, categoryId, canBeLinkedToAccount, ):
        request_args = locals()
        url_template = 'api/{database}/AccountCategoryNVL?categoryId={categoryId}&amp;canBeLinkedToAccount={canBeLinkedToAccount}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_accountCategoryNVL_byCategoryid(self, database, categoryId, ):
        request_args = locals()
        url_template = 'api/{database}/AccountCategoryNVL?categoryId={categoryId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_accountCategoryNVL(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/AccountCategoryNVL'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    