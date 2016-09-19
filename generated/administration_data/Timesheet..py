import requests, json
from generated.base.unit4_base import Unit4Base
class Timesheet.(Unit4Base):


    def get_timesheet_byEmployeeid_and_yearNumber_and_employeeId_and_yearNumber_and_mostRecently(self, database, employeeId, yearNumber, mostRecently, ):
        request_args = locals()
        url_template = 'api/{database}/Timesheet/OpenOrNew/{employeeId}?yearNumber={yearNumber}&amp;mostRecently={mostRecently}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_timesheet_byEmployeeid(self, database, employeeId, ):
        request_args = locals()
        url_template = 'api/{database}/Timesheet/OpenOrNew/{employeeId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{yearNumber}_{weekNumber}_byEmployeeid_and_yearNumber_and_employeeId_and_yearNumber_and_weekNumber(self, database, employeeId, yearNumber, weekNumber, ):
        request_args = locals()
        url_template = 'api/{database}/Timesheet/{employeeId}/{yearNumber}/{weekNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_timesheet(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/Timesheet'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_{yearNumber}_{weekNumber}_byEmployeeid_and_yearNumber_and_employeeId_and_yearNumber_and_weekNumber(self, database, employeeId, yearNumber, weekNumber, ):
        request_args = locals()
        url_template = 'api/{database}/Timesheet/{employeeId}/{yearNumber}/{weekNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    