import requests, json
from generated.base.unit4_base import Unit4Base
class Administration(Unit4Base):


    def delete_administration_byAdministrationid(self, administrationId, ):
        request_args = locals()
        url_template = 'api/Administration/{administrationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administration_byAdministrationid(self, administrationId, ):
        request_args = locals()
        url_template = 'api/Administration/{administrationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_administration(self, ):
        request_args = locals()
        url_template = 'api/Administration'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_administration_byAdministrationid(self, administrationId, ):
        request_args = locals()
        url_template = 'api/Administration/{administrationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def delete_administrationGroup_byGroupid(self, groupId, ):
        request_args = locals()
        url_template = 'api/AdministrationGroup/{groupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationGroup_byGroupid(self, groupId, ):
        request_args = locals()
        url_template = 'api/AdministrationGroup?groupId={groupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationGroup(self, ):
        request_args = locals()
        url_template = 'api/AdministrationGroup'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_administrationGroup(self, ):
        request_args = locals()
        url_template = 'api/AdministrationGroup'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_administrationGroup_byGroupid(self, groupId, ):
        request_args = locals()
        url_template = 'api/AdministrationGroup?groupId={groupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_administrationGroup(self, ):
        request_args = locals()
        url_template = 'api/AdministrationGroup'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationGroupList(self, ):
        request_args = locals()
        url_template = 'api/AdministrationGroupList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationGroupNVL_byUsername(self, userName, ):
        request_args = locals()
        url_template = 'api/AdministrationGroupNVL?userName={userName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationGroupNVL(self, ):
        request_args = locals()
        url_template = 'api/AdministrationGroupNVL'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationInfo_byAdministrationid(self, administrationId, ):
        request_args = locals()
        url_template = 'api/AdministrationInfo/{administrationId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationInfoList_byGroupid(self, groupId, ):
        request_args = locals()
        url_template = 'api/AdministrationInfoList?groupId={groupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationInfoList(self, ):
        request_args = locals()
        url_template = 'api/AdministrationInfoList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationNVL_byUsername_and_groupId(self, userName, groupId, ):
        request_args = locals()
        url_template = 'api/AdministrationNVL/{userName}?groupId={groupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationNVL_byGroupid_and_userName(self, groupId, userName, ):
        request_args = locals()
        url_template = 'api/AdministrationNVL/{groupId}?userName={userName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationNVL_byUsername(self, userName, ):
        request_args = locals()
        url_template = 'api/AdministrationNVL?userName={userName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationNVL_byGroupid(self, groupId, ):
        request_args = locals()
        url_template = 'api/AdministrationNVL?groupId={groupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_administrationNVL(self, ):
        request_args = locals()
        url_template = 'api/AdministrationNVL'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def delete_license_bySupportnumber(self, supportNumber, ):
        request_args = locals()
        url_template = 'api/License/{supportNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_license_byUsername(self, userName, ):
        request_args = locals()
        url_template = 'api/License/Default/{userName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_license_bySupportnumber_and_userName(self, supportNumber, userName, ):
        request_args = locals()
        url_template = 'api/License/{supportNumber}?userName={userName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_license_byUsername_and_supportNumber(self, userName, supportNumber, ):
        request_args = locals()
        url_template = 'api/License/{userName}?supportNumber={supportNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_license_bySupportnumber(self, supportNumber, ):
        request_args = locals()
        url_template = 'api/License?supportNumber={supportNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_license_byUsername(self, userName, ):
        request_args = locals()
        url_template = 'api/License?userName={userName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_license(self, ):
        request_args = locals()
        url_template = 'api/License'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_license(self, ):
        request_args = locals()
        url_template = 'api/License'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_license_bySupportnumber_and_userName(self, supportNumber, userName, ):
        request_args = locals()
        url_template = 'api/License/{supportNumber}?userName={userName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_license_byUsername_and_supportNumber(self, userName, supportNumber, ):
        request_args = locals()
        url_template = 'api/License/{userName}?supportNumber={supportNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_license_bySupportnumber(self, supportNumber, ):
        request_args = locals()
        url_template = 'api/License?supportNumber={supportNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_license_byUsername(self, userName, ):
        request_args = locals()
        url_template = 'api/License?userName={userName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_license(self, ):
        request_args = locals()
        url_template = 'api/License'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_moveAdministrationToGroupCommand_byTargetgroupid(self, targetGroupId, ):
        request_args = locals()
        url_template = 'api/MoveAdministrationToGroupCommand?targetGroupId={targetGroupId}&amp;administrationIds[0]={administrationIds[0]}&amp;administrationIds[1]={administrationIds[1]}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_programRightsCommand_byProgramnumber(self, programNumber, ):
        request_args = locals()
        url_template = 'api/ProgramRightsCommand/CanUserEditInProgram?programNumber={programNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_programRightsCommand_byProgramnumber(self, programNumber, ):
        request_args = locals()
        url_template = 'api/ProgramRightsCommand/CanUserStartProgram?programNumber={programNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_programRightsInfoList_byRightsgroupid_and_languageId(self, rightsGroupId, languageId, ):
        request_args = locals()
        url_template = 'api/ProgramRightsInfoList/{rightsGroupId}?languageId={languageId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_programRightsInfoList_byRightsgroupid(self, rightsGroupId, ):
        request_args = locals()
        url_template = 'api/ProgramRightsInfoList/{rightsGroupId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_sessionInfo(self, ):
        request_args = locals()
        url_template = 'api/SessionInfo'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_systemVersionInfo(self, ):
        request_args = locals()
        url_template = 'api/SystemVersionInfo'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def delete_user_byUserid(self, userId, ):
        request_args = locals()
        url_template = 'api/User/{userId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_user_byUserid(self, userId, ):
        request_args = locals()
        url_template = 'api/User/{userId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_user(self, ):
        request_args = locals()
        url_template = 'api/User'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_user_byUserid(self, userId, ):
        request_args = locals()
        url_template = 'api/User/{userId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_userInfo_byUserid(self, userId, ):
        request_args = locals()
        url_template = 'api/UserInfo?userId={userId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_userInfo(self, ):
        request_args = locals()
        url_template = 'api/UserInfo'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_userNVL(self, ):
        request_args = locals()
        url_template = 'api/UserNVL'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def delete_viewState_byViewname_and_viewStateId_and_viewStateId_and_index_and_controlName(self, viewName, viewStateId, index, controlName, ):
        request_args = locals()
        url_template = 'api/ViewState/{viewName}/{viewStateId}/{index}?controlName={controlName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def delete_viewState_byViewname_and_viewStateId_and_viewStateId_and_index(self, viewName, viewStateId, index, ):
        request_args = locals()
        url_template = 'api/ViewState/{viewName}/{viewStateId}/{index}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_viewState_byViewname_and_viewStateId_and_viewStateId_and_index_and_controlName(self, viewName, viewStateId, index, controlName, ):
        request_args = locals()
        url_template = 'api/ViewState/{viewName}/{viewStateId}/{index}?controlName={controlName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_viewState_byViewname_and_viewStateId_and_viewStateId_and_index(self, viewName, viewStateId, index, ):
        request_args = locals()
        url_template = 'api/ViewState/{viewName}/{viewStateId}/{index}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_viewState(self, ):
        request_args = locals()
        url_template = 'api/ViewState'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_viewState_byViewname_and_viewStateId_and_viewStateId_and_index_and_controlName(self, viewName, viewStateId, index, controlName, ):
        request_args = locals()
        url_template = 'api/ViewState/{viewName}/{viewStateId}/{index}?controlName={controlName}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_viewState_byViewname_and_viewStateId_and_viewStateId_and_index(self, viewName, viewStateId, index, ):
        request_args = locals()
        url_template = 'api/ViewState/{viewName}/{viewStateId}/{index}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_viewStateList_byViewname_and_viewStateId(self, viewName, viewStateId, ):
        request_args = locals()
        url_template = 'api/ViewStateList/{viewName}/{viewStateId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_viewStateList(self, ):
        request_args = locals()
        url_template = 'api/ViewStateList'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    