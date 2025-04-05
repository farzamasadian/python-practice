import re
# str = 'salam jadi. salam mehdi. Salam Sara. salam soosan.'
# result = re.findall(r'salam',str)
# print(result)

# input='farzamfarzam@gmail.com'
# result=re.search(r'.+\@.+\..{2,3}',input)
# print(result)

# str = '''The price of oil is 65$ for 3boshke for yesterday
# The price of oil is 74$ for 3boshke for today
# The price of oil is 61$ for 3boshke for 9/4'''
# result=re.findall(r'The price of oil is (\d+)\$ for (\d+)boshke for(.*)',str)
# print(result)
# for price, boshke, day in result:
#     print(price, boshke, day)

# str = 'salam jadi. salam mehdi. Salam Sara. salam soosan.'
# result = re.sub(r'[Ss]alam (\w+)\.','Hi \g<1>',str)
# print(result)

# str = '''The price of oil is 65$ for 3boshke for yesterday
# The price of oil is 74$ for 3boshke for today
# The price of oil is 61$ for 3boshke for 9/4'''
# replace_str=r'The price of oil is (\d+)\$ for (\d+)boshke for(.*)'
# result=re.sub(replace_str,'\g<3>,\g<1>,\g<2>',str)
# print(result)