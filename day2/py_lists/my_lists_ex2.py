my_list = ["Do", "your", "homework", "now", "kids"]

my_list.append("please")
my_list.append("Do")

first = my_list.pop(0)

my_list.sort()

print("-" * 50)
print(my_list)
print("-" * 50)

print()
for i, val in enumerate(my_list):
    print(f"{i:>3} -> {val:>15}")
print()
