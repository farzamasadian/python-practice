from collections import OrderedDict
od = OrderedDict()
n = int(input('Please enter the total votes'))
for i in range(n):
    m = input('Please enter the name of the country')
    od[m] = od.get(m,0)+1
countries = list(od.keys())
countries.sort()
{print(each,od[each]) for each in countries}
    # print(each,od[each])