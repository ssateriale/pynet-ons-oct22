my_ipaddress = ["192.168.1.1", "10.1.1.1", "172.16.31.254", "8.8.8.8", "8.8.4.4"]
my_ipaddress.append("10.10.10.10")
my_ipaddress.extend(["1.1.1.1", "1.1.1.2"])
my_ipaddress = my_ipaddress + ["172.16.1.1", "172.16.1.2"]
print(my_ipaddress)

print(my_ipaddress[0])
print(my_ipaddress[-1])

first_ip = my_ipaddress.pop(0)
last_ip = my_ipaddress.pop()

my_ipaddress[0] = "2.2.2.2"
print(my_ipaddress[0])
