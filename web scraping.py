# import re
# pattern=r'^90094.*85394'
# tex="486523756248752638576230874562834658345682743525"
# result=re.search(pattern,tex)
# if result:
#     print("yes")
# else:
#     print("no")



# import re
# pattern=r'^[a-zA-Z0-9$%*.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'
# email="khushisahu0089@gmail.com"
# met = re.match(pattern , email)
# if met:
#     print("yes:",met.group())

# else:
#     print("no")    

# import re
# pattern=r'^(\+91-)?\d{3}\d{3}\d{4}$'
# phonenum="9009485394"
# met = re.match(pattern , phonenum)
# if met:
#     print("yes:",met.group())

# else:
#     print("no")



import re
password=r'^(\+91)?\d{3}\d{3}\d{4}+$'
phonenumber="9691407355"
met=re.match(password,phonenumber)
if met:
    print("yes",met.group())
else:
    print("no")




# import re
# passward=r'^@[a-zA-Z0-9]+[a-zA-Z0-9#@]+$'
# user_id="@khushisahu0089"
# met=re.match(passward,user_id)
# if met:
#     print("yes its same same ",met.group())
# else:
#     print("no its not same same")





import re 
pattern=r'^[a-zA-Z0-9]+[a-zA-Z0-9#@_]+[a-zA-Z0-9]+\.[a-zA-Z0-9_@#]+$'
passward="khushir0089#@_sahu.its_me"
result=re.match(pattern,passward)
if result:
    print("yes its true",result.group())
else:
    print("no its false")


# import requests
# from bs4 import BeautifulSoup
# url='https://www.tutorialsfreak.com/'
# web=requests.get(url)
# print(web.status_code) #check permission
# print(web.content) #print content of web
# print(web.text) #print text of web

# soup=BeautifulSoup(web.content,"html.parser") # data parsing in html
# print(soup)


import requests
from bs4 import BeautifulSoup
url='https://edunetfoundation.org/'
web=requests.get(url)
print(web.status_code)
print(web.content)
print(web.text)

soup=BeautifulSoup(web.content,"html.parser")
print(soup)