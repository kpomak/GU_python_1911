# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#   |--settings
#   |--mainapp
#   |--adminapp
#   |--authapp


import os

starter = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for key, value in starter.items():
    for dir_name in value:
        dir_path = os.path.join(key, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
