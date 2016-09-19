import os


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
GENERATED_OUTPUT_DIRNAME = 'generated'
EXTRACTED_OUTPUT_DIRNAME = 'extracted'
PYTHON_CLASS_TEMPLATE_NAME = 'unit4_python_class.template'


GENERATED_OUTPUT_DIR = os.path.join(ROOT_DIR, GENERATED_OUTPUT_DIRNAME)
EXTRACTED_OUTPUT_DIR = os.path.join(ROOT_DIR, EXTRACTED_OUTPUT_DIRNAME)
PYTHON_CLASS_TEMPLATE = os.path.join(ROOT_DIR, 'library_generator', PYTHON_CLASS_TEMPLATE_NAME)


