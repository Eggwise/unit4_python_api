import json, jinja2, os
from jinja2 import Environment
from jinja2 import PackageLoader
from library_generator.class_definition_generator import generate_class_definition
from settings import EXTRACTED_OUTPUT_DIR, PYTHON_CLASS_TEMPLATE, GENERATED_OUTPUT_DIR


with open(PYTHON_CLASS_TEMPLATE) as tf:
    template_source = tf.read()
    template = jinja2.Template(source=template_source)



EXTRACTED_DATA_FILENAME = 'extracted_modules.json'
EXTRACTED_DATA_FILE = os.path.join(EXTRACTED_OUTPUT_DIR, EXTRACTED_DATA_FILENAME )


BASECLASS = 'Unit4Base'
ROOT_MODULE = 'generated'

with open(EXTRACTED_DATA_FILE) as f:
    api_data = json.loads(f.read())
    for module_data in api_data:

        module_name = module_data['module_name']
        print(module_name)

        module_path = os.path.join(GENERATED_OUTPUT_DIR, module_name)

        if not os.path.exists(module_path):
            os.makedirs(module_path)

        classes = module_data['classes']
        for c in classes:
            class_definition = generate_class_definition(c)
            class_definition['base_class'] = BASECLASS
            class_definition['root_module'] = ROOT_MODULE

            rendered_python_class = template.render(**class_definition)

            python_class_filename = class_definition['class_name'] + '.py'
            python_class_filepath = os.path.join(module_path, python_class_filename)

            with open(python_class_filepath, 'w') as pcf:
                pcf.write(rendered_python_class)
