"""
Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения <request_type>, информации вида:
<requested_resource>,
(<remote_addr>,
<response_code>,
<request_datetime>,
<response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET
/downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
'/downloads/product_2', '304', '0')
15Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
"""

import re

PATTERN_STRING = re.compile(r'(^(?:\d{1,3}\.){3}\d{1,3})|((?:(?:[0-9a-f]){0,4}:){7}[0-9a-f]{1,4})'
                            r'|(HEAD|GET)|(?<=\[)[^\]]+(?=\])'
                            r'|(/downloads[^"]+)|(?<=\s)\d+(?=\s)|(?<=\d{3}\s)\d+(?=\s)')

with open('nginx_logs', encoding='utf-8') as f:
    for line in f:
        result = PATTERN_STRING.finditer(line)
        parsed_raw = tuple(map(lambda x: x.group(0), result))
        print(parsed_raw)

# ...
# ('54.76.150.33', '04/Jun/2015:03:06:22 +0000', 'GET', '/downloads/product_1 HTTP/1.1', '404', '336')
# ('54.76.150.33', '04/Jun/2015:03:06:43 +0000', 'GET', '/downloads/product_1 HTTP/1.1', '404', '333')
# ('2001:4800:7815:102:8bee:6e66:ff05:215f', '04/Jun/2015:03:06:36 +0000', 'GET', '/downloads/product_1 HTTP/1.1', '200', '85619205')
# ('185.40.8.59', '04/Jun/2015:03:06:02 +0000', 'GET', '/downloads/product_2 HTTP/1.1', '304', '0')
# ('185.40.8.59', '04/Jun/2015:03:06:52 +0000', 'GET', '/downloads/product_2 HTTP/1.1', '304', '0')
# ...