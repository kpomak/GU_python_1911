# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).


request_list = []
with open('nginx_logs.txt') as f:
    for line in f:
        log_parse = line.split()
        ip_address, request_type, request_resource = log_parse[0], log_parse[5][1:], log_parse[6]
        request_list.append((ip_address, request_type, request_resource))

print(request_list[0:3])

# [('93.180.71.3', 'GET', '/downloads/product_1'),
#  ('217.168.17.5', 'GET', '/downloads/product_1'),
#  ('93.180.71.3', 'GET', '/downloads/product_1')]
