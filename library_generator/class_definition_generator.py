import json

# Deze functie genereert de methode definitie aan de hand van de endpoint data
# TODO , een mooi formaat genereren voor de methodenamen, rekening houdend met dubbele namen, parameters etc.
def generate_python_method(endpoint_data):
    url_api = endpoint_data['url_api']
    url_doc = endpoint_data['url_doc']
    arguments = endpoint_data['arguments']
    method = endpoint_data['method']


    request_method_mapping = {
        'POST' : 'create',
        'PUT': 'update',
        'GET': 'get',
        'DELETE': 'delete'
    }

    #example 2
    #SplitJournalEntryCommand/Revert?fiscalYear={fiscalYear}&amp;journalId={journalId}
    #must become splitJournalEntryCommand_Revert_byFiscalyearId_journalId
    #not very pythonic.. function splitJournalEntryCommandRevert(fiscalyear_id, journal_id) would be better..


    #build method name
    method_name_template = '{method}'
    url_api_split = url_api.split('/')
    if 'database' in url_api:
        url_api_split = url_api_split[2:]
    else:
        url_api_split = url_api_split[1:]

    # print(url_api_split)
    if 'database' in url_api:
        #
        #
        #
        # url_api_split2 = url_api.split('?')
        # url_api_split2 = '_'.join(url_api_split2[0].split('/')[1:])
        # print(url_api_split2, method, arguments)

        #see example 2
        if len(url_api_split) > 3:
            # print(url_api_split)
            method_name_base = url_api_split[2] + '_' + url_api_split[3].split('?')[0]
        else:
            method_name_base = url_api.split('/')[2].split('?')[0]
    else:
        method_name_base = url_api.split('/')[1].split('?')[0]

    #lower first letter
    method_name_base = method_name_base[0].lower() + method_name_base[1:]
    # method_name_base = method_name_template.format(method=method.lower())

    #add req_method type to beginning of py method name
    method_name_base = request_method_mapping[method] + '_{0}'.format(method_name_base)

    arguments_to_skip = ['database']
    arguments_to_process =[a for a in arguments if a not in arguments_to_skip]
    # print(arguments_to_process)

    def method_name_1_arg_extension(args):
        method_name_extension = '_by{param}'.format(param=args[0].capitalize())
        return method_name_extension

    if len(arguments_to_process) == 0:
        method_name = method_name_base
        # print(endpoint_data)

    #if more args to skip, check length without the skipped args and compare with that
    #if one extra param
    if len(arguments_to_process) == 1:
        #for now the extra param is the second in the list, cuz len args to skip == 1
        method_name = method_name_base + method_name_1_arg_extension(arguments_to_process)
        # print(method_name)

    if len(arguments_to_process) == 2:
        method_name = method_name_base + method_name_1_arg_extension(arguments_to_process)
        method_name = method_name + '_and_{0}'.format(arguments_to_process[1])
        # print(method_name)

    if len(arguments_to_process) >= 3:
        method_name = method_name_base + method_name_1_arg_extension(arguments_to_process)
        method_name = method_name + '_and_{0}'.format(arguments_to_process[1])
        for a in arguments[1:]:
            method_name += '_and_{0}'.format(a)


    method = {**endpoint_data, **dict(type=method.lower(), name=method_name, api_url=url_api, arguments = arguments)}
    return method
    # print(method_name)
    # print(locals())



def generate_class_definition(class_config):
    class_name = class_config['name']
    endpoints = class_config['endpoints']

    methods = [generate_python_method(e) for e in endpoints]
    return dict(class_name=class_name, methods=methods)