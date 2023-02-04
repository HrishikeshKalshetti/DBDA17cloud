'''
<  left align
> right align
^ center align

print("Apple {:20} is Great".format("Ooty"))
print("Apple {:<20} is Great".format("Ooty"))
print("Apple {:>20} is Great".format("Ooty"))
print("Apple {:^20} is Great".format("Ooty"))
'''
width = 50
price_width = 10
items_width = width - price_width
header_fmt = '{{:{}}}{{:>{}}}'
header_fmt = header_fmt.format(items_width, price_width)
fmt = "{{:{}}}{{:{}}}".format(items_width, price_width)
# print(fmt)
# print(header_fmt)
print('_' * width)
print(header_fmt.format("Items", "Price"))
print('_' * width)
print(fmt.format("Apple", 150))
print(fmt.format("Orange", 240))
print(fmt.format("Pine", 120))
print(fmt.format("Mango", 500))
print(fmt.format("Prunes", 150))
print("=" * width)
