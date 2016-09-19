import requests, json
from generated.base.unit4_base import Unit4Base
class OrderInfo(Unit4Base):


    def get_orderInfoList_byProjectid(self, database, projectId, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfoList/ByProjectId/{projectId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_orderInfoList_byCustomerid(self, database, customerId, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfoList/OpenOrders?customerId={customerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_orderInfoList(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfoList/OpenOrders'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_{minDate}_{maxDate}_byCustomerid_and_minDate_and_customerId_and_minDate_and_maxDate_and_minPrice_and_maxPrice_and_fiscalYear_and_onlyOpen_and_PageSize_and_PageNumber(self, database, customerId, minDate, maxDate, minPrice, maxPrice, fiscalYear, onlyOpen, PageSize, PageNumber, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfoList/{customerId}/{minDate}/{maxDate}/{minPrice}/{maxPrice}/{fiscalYear}/{onlyOpen}?PageSize={PageSize}&amp;PageNumber={PageNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_orderInfoList_byCustomerid_and_fiscalYear_and_customerId_and_fiscalYear_and_minDate_and_maxDate_and_minPrice_and_maxPrice_and_onlyOpen_and_PageSize_and_PageNumber(self, database, customerId, fiscalYear, minDate, maxDate, minPrice, maxPrice, onlyOpen, PageSize, PageNumber, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfoList/{customerId}/{fiscalYear}?minDate={minDate}&amp;maxDate={maxDate}&amp;minPrice={minPrice}&amp;maxPrice={maxPrice}&amp;onlyOpen={onlyOpen}&amp;PageSize={PageSize}&amp;PageNumber={PageNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_orderInfoList_byCustomerid_and_fiscalYear_and_customerId_and_fiscalYear_and_minDate_and_maxDate_and_minPrice_and_maxPrice_and_onlyOpen(self, database, customerId, fiscalYear, minDate, maxDate, minPrice, maxPrice, onlyOpen, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfoList/{customerId}/{fiscalYear}?minDate={minDate}&amp;maxDate={maxDate}&amp;minPrice={minPrice}&amp;maxPrice={maxPrice}&amp;onlyOpen={onlyOpen}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_orderInfoList_byCustomerid_and_minDate_and_customerId_and_minDate_and_maxDate_and_minPrice_and_maxPrice_and_fiscalYear_and_onlyOpen_and_PageSize_and_PageNumber(self, database, customerId, minDate, maxDate, minPrice, maxPrice, fiscalYear, onlyOpen, PageSize, PageNumber, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfoList/{customerId}?minDate={minDate}&amp;maxDate={maxDate}&amp;minPrice={minPrice}&amp;maxPrice={maxPrice}&amp;fiscalYear={fiscalYear}&amp;onlyOpen={onlyOpen}&amp;PageSize={PageSize}&amp;PageNumber={PageNumber}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_orderInfoList_byCustomerid_and_minDate_and_customerId_and_minDate_and_maxDate_and_minPrice_and_maxPrice_and_fiscalYear_and_onlyOpen(self, database, customerId, minDate, maxDate, minPrice, maxPrice, fiscalYear, onlyOpen, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfoList/{customerId}?minDate={minDate}&amp;maxDate={maxDate}&amp;minPrice={minPrice}&amp;maxPrice={maxPrice}&amp;fiscalYear={fiscalYear}&amp;onlyOpen={onlyOpen}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_orderInfoList_byCustomerid_and_fiscalYear(self, database, customerId, fiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfoList/{customerId}?fiscalYear={fiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    def get_orderInfoList_byCustomerid(self, database, customerId, ):
        request_args = locals()
        url_template = 'api/{database}/OrderInfoList/{customerId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.get(url=url)
        print(response.text)

        return json.loads(response.text)
    