import requests, lxml, re
from lxml.html import etree
import json

DOC_URL = 'https://api.online.unit4.nl/v182/help/'


def get_all_classes(page_tree):
    general_data_xpath = '//*[@id="body"]/section[2]/div[2]'
    commands_xpath = '//*[@id="body"]/section[2]/div[6]'
    administration_data_xpath = '//*[@id="body"]/section[2]/div[4]/div'
    documents_xpath = '//*[@id="body"]/section[2]/div[8]'

    modules_configs = (
        dict(title='General Data', module_name='general_data', xpath=general_data_xpath),
        dict(title='Commands', module_name='commands', xpath=commands_xpath),
        dict(title='Documents', module_name='documents', xpath=documents_xpath),
        dict(title='Administration Data', module_name='administration_data', xpath=administration_data_xpath)
    )
    modules = []
    for m_config in modules_configs:
        classes = get_api_classes(m_config['xpath'], page_tree)
        del (m_config['xpath'])
        m_config['classes'] = classes
        modules.append(m_config)

    with open('extracted_modules.json', 'w') as f:
        f.write(json.dumps(modules))


def get_api_classes(data_xpath, doc_page_tree):
    classes_container = doc_page_tree.xpath(data_xpath)
    classes = []
    for class_html in classes_container:
        el_string = str(etree.tostring(class_html))

        endpoints = []
        # get classes from container tree
        element_split = el_string.split()

        for e in element_split:
            if e.startswith('href'):
                url_doc = e.split('"')[1]
                url_api = e.split('>')[1].split('</')[0]

                method = url_doc.split('Api/')[1].split('-')[0]
                arguments = re.findall('{([a-zA-Z]+)}', url_api)

                endpoint = dict(url_api=url_api, url_doc=url_doc, method=method, arguments=arguments)
                endpoints.append(endpoint)

        # get class name from description

        # case description is
        # Gets a name value list of ClassName that matches the specified criteria
        class_name = re.findall(' the specified (.*)', el_string)

        # in case description = Execute the ClassName...
        if len(class_name) == 0:
            class_name = re.findall('Execute the (.*)', el_string)

        class_name = class_name[0]
        # case description is
        # Gets a name value list of ClassName that matches the specified criteria
        if class_name.startswith('criteria'):
            class_name = re.findall('list of (.*) that', el_string)[0]

        class_name = class_name.split()[0].strip()
        unit4_class = dict(name=class_name, endpoints=endpoints)

        classes.append(unit4_class)

    return classes


def scrape_unit4_modules(url):
    response = requests.get(url)
    html = ''.join(response.text.splitlines()[1:])
    parser = etree.HTMLParser()
    tree = etree.HTML(html, parser)
    get_all_classes(tree)


scrape_unit4_modules(DOC_URL)
