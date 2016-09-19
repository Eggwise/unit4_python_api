import requests, json
from generated.base.unit4_base import Unit4Base
class EmployeeInfo(Unit4Base):


    def get_employeeInfoList_byMustdeclarehoursonly(self, database, mustDeclareHoursOnly, ):
        request_args = locals()
        url_template = 'api/{database}/EmployeeInfoList/ApprovableByMe?mustDeclareHoursOnly={mustDeclareHoursOnly}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_employeeInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/EmployeeInfoList/ApprovableByMe'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_employeeInfoList_byDepartmentid_and_mustDeclareHoursOnly(self, database, departmentId, mustDeclareHoursOnly, ):
        request_args = locals()
        url_template = 'api/{database}/EmployeeInfoList/ByDepartment/{departmentId}?mustDeclareHoursOnly={mustDeclareHoursOnly}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_employeeInfoList_byDepartmentid(self, database, departmentId, ):
        request_args = locals()
        url_template = 'api/{database}/EmployeeInfoList/ByDepartment/{departmentId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_employeeInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/EmployeeInfoList/ByMustDeclareHours'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_employeeInfoList_byName_and_searchName(self, database, name, searchName, ):
        request_args = locals()
        url_template = 'api/{database}/EmployeeInfoList/ByName/{name}?searchName={searchName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_employeeInfoList_byName(self, database, name, ):
        request_args = locals()
        url_template = 'api/{database}/EmployeeInfoList/ByName/{name}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_employeeInfoList_bySearchname(self, database, searchName, ):
        request_args = locals()
        url_template = 'api/{database}/EmployeeInfoList/BySearchName/{searchName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_employeeInfoList_byEmployeeid(self, database, employeeId, ):
        request_args = locals()
        url_template = 'api/{database}/EmployeeInfoList?employeeId={employeeId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_employeeInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/EmployeeInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    