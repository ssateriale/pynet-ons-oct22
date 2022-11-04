def split_ip(ip_addr, message):
    print(message)
    octets = ip_addr.split(".")
    return octets


my_octets = split_ip("1.1.1.1", "Splitting IP Addresses")
print(my_octets)
