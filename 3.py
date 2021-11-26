# Написать скрипт, который собирает все шаблоны в одну папку
# templates, например:
# |--my_project
# ...
# |--templates
# ||--mainapp
# |||--base.html
# |||--index.html
# ||--authapp
# ||--base.html
# ||--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
# расположены в родительских папках (они играют роль пространств имён); предусмотреть
# возможные исключительные ситуации.


import os
import shutil


templates_list = [os.path.dirname(root) for root, dirs, files in os.walk('my_project')
                  if 'index.html' in files and 'base.html' in files]
for root in templates_list:
    shutil.copytree(root, 'templates', dirs_exist_ok=True)

