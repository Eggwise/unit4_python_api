import requests, json
from generated.base.unit4_base import Unit4Base
class LanguageNVL(Unit4Base):


    def get_languageNVL(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/LanguageNVL'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    