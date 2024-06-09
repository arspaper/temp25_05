import ipaddress


count = 0
network = ipaddress.ip_network('122.159.136.144/255.255.255.248')
b_address = list()
for address in network:
    binary_string = f'{int(address):b}'
    b_address.append(binary_string)

for address in b_address:
    if address.count('1') % 4 != 0:
        count += 1

print(count)