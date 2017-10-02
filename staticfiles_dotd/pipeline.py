import os

from django.template import engines


def django_template_engine(filename, contents):
    if not os.path.splitext(filename)[1] in ('.html', '.css', '.js'):
        return contents

    template = engines['django'].from_string(contents.decode('utf-8'))

    return template.render({}).encode('utf-8')
