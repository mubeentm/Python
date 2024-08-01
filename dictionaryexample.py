my_stock_list={"TCS":2700,"Infosys":3000,"IDBI":140,"NTPC":220}
# print(type(my_stock_list))
my_stock_list["SBI"]=1700
print(my_stock_list)
print(len(my_stock_list))
print(my_stock_list.keys())
print(my_stock_list.values())

for stock in my_stock_list:
    print(stock, "has price",my_stock_list[stock])

for stock in my_stock_list.items():
    print(stock)
    print(stock[0])

print(my_stock_list.items())#it will return list of tuples

for key,value in my_stock_list.items():
    print(key," -> ",value)

print(my_stock_list.pop("Infosys"))#remove the key value pair mentioned in the key
print(my_stock_list.popitem())#remove the last item from the dict
print(my_stock_list)



del my_stock_list["TCS"]
for key,value in my_stock_list.items():
    print(key," -> ",value)


# swapping values

swapped = {}
for key,value in my_stock_list.items():
    swapped[value]=key
    print(swapped)