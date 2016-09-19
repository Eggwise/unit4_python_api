import requests, json
from generated.base.unit4_base import Unit4Base
class Language(Unit4Base):


    def delete_language_byLanguageid(self, database, languageId, ):
        request_args = locals()
        url_template = 'api/{database}/Language/{languageId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_language_byLanguageid(self, database, languageId, ):
        request_args = locals()
        url_template = 'api/{database}/Language/{languageId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_language(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Language'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_language_byLanguageid(self, database, languageId, ):
        request_args = locals()
        url_template = 'api/{database}/Language/{languageId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    