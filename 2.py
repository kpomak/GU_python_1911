# Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
# даже с файлами, размер которых превышает объем ОЗУ компьютера.


with open('nginx_logs.txt') as f:
    request_list = [line.split()[0] for line in f]

most_common, spammer_ip, request_set = 0, '', set(request_list)

for ip_address in request_set:
    if request_list.count(ip_address) > most_common:
        most_common, spammer_ip = request_list.count(ip_address), ip_address

print(f'C IP-адреса {spammer_ip} поступило {most_common} запросов')

# C IP-адреса 216.46.173.126 поступило 2350 запросов
