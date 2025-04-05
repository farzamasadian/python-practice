import re
str = 'This is an advanced Python programming in Maktabkhooneh.'
result = re.sub(r'Maktabkhooneh','university',str)
print(result)