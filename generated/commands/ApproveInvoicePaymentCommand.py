import requests, json
from generated.base.unit4_base import Unit4Base
class ApproveInvoicePaymentCommand(Unit4Base):


    def create_approveInvoicePaymentCommand_byInvoiceid_and_approverId(self, database, invoiceId, approverId, ):
        request_args = locals()
        url_template = 'api/{database}/ApproveInvoicePaymentCommand?invoiceId={invoiceId}&amp;approverId={approverId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_calcSpecPriceCommand_byCustomerid_and_productId_and_customerId_and_productId_and_currencyId_and_quantity_and_orderDate_and_vatIncluded_and_projectId(self, database, customerId, productId, currencyId, quantity, orderDate, vatIncluded, projectId, ):
        request_args = locals()
        url_template = 'api/{database}/CalcSpecPriceCommand?customerId={customerId}&amp;productId={productId}&amp;currencyId={currencyId}&amp;quantity={quantity}&amp;orderDate={orderDate}&amp;vatIncluded={vatIncluded}&amp;projectId={projectId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_createPaymentFileCommand_byBankid(self, database, bankId, ):
        request_args = locals()
        url_template = 'api/{database}/CreatePaymentFileCommand?bankId={bankId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_dmDocumentCreateReferenceCommand_byType(self, database, type, ):
        request_args = locals()
        url_template = 'api/{database}/DmDocumentCreateReferenceCommand?type={type}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_getCustomerIdCommand(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/GetCustomerIdCommand'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_getInvoiceIdCommand(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/GetInvoiceIdCommand'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_getMandateIdCommand(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/GetMandateIdCommand'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_getNextJournalTransactionCommand_byFiscalyear_and_journalId(self, database, fiscalYear, journalId, ):
        request_args = locals()
        url_template = 'api/{database}/GetNextJournalTransactionCommand?fiscalYear={fiscalYear}&amp;journalId={journalId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_getPersonIdCommand(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/GetPersonIdCommand'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_getSupplierIdCommand(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/GetSupplierIdCommand'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_incrementPaymentReminderCounterCommand_byInvoiceid(self, database, invoiceId, ):
        request_args = locals()
        url_template = 'api/{database}/IncrementPaymentReminderCounterCommand?invoiceId={invoiceId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_incrementPrintCounterCommand_byPrintentitytype_and_entityId(self, database, printEntityType, entityId, ):
        request_args = locals()
        url_template = 'api/{database}/IncrementPrintCounterCommand?printEntityType={printEntityType}&amp;entityId={entityId}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_mailMessageCountCommand(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/MailMessageCountCommand?statesCriteria[0]={statesCriteria[0]}&amp;statesCriteria[1]={statesCriteria[1]}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_modifyAutoIdCommand_byType(self, database, type, ):
        request_args = locals()
        url_template = 'api/{database}/ModifyAutoIdCommand/Disable?type={type}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_modifyAutoIdCommand_byType_and_startId_and_type_and_startId_and_interval_and_length_and_useLeadingZeroes(self, database, type, startId, interval, length, useLeadingZeroes, ):
        request_args = locals()
        url_template = 'api/{database}/ModifyAutoIdCommand/Enable?type={type}&amp;startId={startId}&amp;interval={interval}&amp;length={length}&amp;useLeadingZeroes={useLeadingZeroes}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_processOrderCommand_byJournalid_and_fiscalYear_and_journalId_and_fiscalYear_and_periodNumber_and_invoiceDate_and_orderId_and_journalTransaction(self, database, journalId, fiscalYear, periodNumber, invoiceDate, orderId, journalTransaction, ):
        request_args = locals()
        url_template = 'api/{database}/ProcessOrderCommand?journalId={journalId}&amp;fiscalYear={fiscalYear}&amp;periodNumber={periodNumber}&amp;invoiceDate={invoiceDate}&amp;orderId={orderId}&amp;journalTransaction={journalTransaction}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_setIsPreferredBankCommand_byBankid_and_isPreferred(self, database, bankId, isPreferred, ):
        request_args = locals()
        url_template = 'api/{database}/SetIsPreferredBankCommand?bankId={bankId}&amp;isPreferred={isPreferred}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_smtpClientConfigurationPresentCommand(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/SmtpClientConfigurationPresentCommand'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_splitJournalEntryCommand_byFiscalyear_and_journalId_and_fiscalYear_and_journalId_and_journalTransaction_and_sequenceNumber_and_targetFiscalYear(self, database, fiscalYear, journalId, journalTransaction, sequenceNumber, targetFiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/SplitJournalEntryCommand?fiscalYear={fiscalYear}&amp;journalId={journalId}&amp;journalTransaction={journalTransaction}&amp;sequenceNumber={sequenceNumber}&amp;targetFiscalYear={targetFiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_splitJournalEntryCommand_byFiscalyear_and_journalId_and_fiscalYear_and_journalId_and_journalTransaction_and_sequenceNumber_and_targetFiscalYear(self, database, fiscalYear, journalId, journalTransaction, sequenceNumber, targetFiscalYear, ):
        request_args = locals()
        url_template = 'api/{database}/SplitJournalEntryCommand/Revert?fiscalYear={fiscalYear}&amp;journalId={journalId}&amp;journalTransaction={journalTransaction}&amp;sequenceNumber={sequenceNumber}&amp;targetFiscalYear={targetFiscalYear}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_updateKeyPerformanceBenchmarkCommand_byKeyperformanceindicatorid_and_value(self, database, keyPerformanceIndicatorId, value, ):
        request_args = locals()
        url_template = 'api/{database}/UpdateKeyPerformanceBenchmarkCommand?keyPerformanceIndicatorId={keyPerformanceIndicatorId}&amp;value={value}'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    def create_validSmtpClientConfigurationCommand(self, database, ):
        request_args = locals()
        url_template = 'api/{database}/ValidSmtpClientConfigurationCommand'
        url = url_template.format(**request_args)
        #print(url)

        url = self.authorize(url)
        response = requests.post(url=url)
        print(response.text)

        return json.loads(response.text)
    