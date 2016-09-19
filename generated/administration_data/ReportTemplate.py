import requests, json
from generated.base.unit4_base import Unit4Base
class ReportTemplate(Unit4Base):


    def delete_reportTemplate_byReporttemplateid(self, database, reportTemplateId, ):
        request_args = locals()
        url_template = 'api/{database}/ReportTemplate/{reportTemplateId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.delete(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_reportTemplate_byReporttype_and_languageId(self, database, reportType, languageId, ):
        request_args = locals()
        url_template = 'api/{database}/ReportTemplate/{reportType}/{languageId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_reportTemplate_byReporttype_and_languageId_and_reportType_and_languageId_and_reportTemplateId(self, database, reportType, languageId, reportTemplateId, ):
        request_args = locals()
        url_template = 'api/{database}/ReportTemplate/{reportType}/{languageId}?reportTemplateId={reportTemplateId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_reportTemplate_byReporttemplateid_and_reportType_and_reportTemplateId_and_reportType_and_languageId(self, database, reportTemplateId, reportType, languageId, ):
        request_args = locals()
        url_template = 'api/{database}/ReportTemplate/{reportTemplateId}?reportType={reportType}&amp;languageId={languageId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_reportTemplate_byReporttemplateid(self, database, reportTemplateId, ):
        request_args = locals()
        url_template = 'api/{database}/ReportTemplate/{reportTemplateId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_reportTemplate(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/ReportTemplate'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_reportTemplate_byReporttype_and_languageId(self, database, reportType, languageId, ):
        request_args = locals()
        url_template = 'api/{database}/ReportTemplate/{reportType}/{languageId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_reportTemplate_byReporttype_and_languageId_and_reportType_and_languageId_and_reportTemplateId(self, database, reportType, languageId, reportTemplateId, ):
        request_args = locals()
        url_template = 'api/{database}/ReportTemplate/{reportType}/{languageId}?reportTemplateId={reportTemplateId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_reportTemplate_byReporttemplateid_and_reportType_and_reportTemplateId_and_reportType_and_languageId(self, database, reportTemplateId, reportType, languageId, ):
        request_args = locals()
        url_template = 'api/{database}/ReportTemplate/{reportTemplateId}?reportType={reportType}&amp;languageId={languageId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    def update_reportTemplate_byReporttemplateid(self, database, reportTemplateId, ):
        request_args = locals()
        url_template = 'api/{database}/ReportTemplate/{reportTemplateId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.put(url=url)
        print(response.text)

        return json.loads(response.text)
    