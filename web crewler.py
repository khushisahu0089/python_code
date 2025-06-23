# import re
# pattern=r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'
# email="anjaligarothiya8@gmail.com"
# met=re.match(pattern,email)
# if met:
#     print("yes",met.group())
# else:
#     print("no")

# import requests
# from bs4 import BeautifulSoup
# url='https://www.primevideo.com/'
# web=requests.get(url)
# print(web.status_code)
# print(web.content)
# print(web.text)

# soup=BeautifulSoup(web.content,"html.parser")
# print(soup)



# # web crawler
# import requests
# from bs4 import BeautifulSoup

# def simple_crawler(url):
#     response=requests.get(url)

#     if response.status_code !=200:
#         print("failed")
#         return
    
#     soup=BeautifulSoup(response.text,"html.parser")

#     for link in soup.find_all('a'):
#         href=link.get('href')
#         if href:
#             print(href)

# simple_crawler('https://web.whatsapp.com/')



# import requests
# from bs4 import BeautifulSoup

# url='https://web.whatsapp.com/'
# response=requests.get(url)

# if response.status_code == 200:
#     soup=BeautifulSoup(response.text,"html.parser")
#     for link in soup.find_all('a'):
#         href=link.get('href')
#         if href:
#             print(href)



# import requests
# from bs4 import BeautifulSoup
# url='https://web.whatsapp.com/'
# response=requests.get(url)

# if response.status_code == 200:
#     soup=BeautifulSoup(response.text,"html.parser")
#     for link in soup.find_all('a'):
#         href=link.get('href')
#         if href:
#             print(href)


# import requests
# from bs4 import BeautifulSoup
# url='https://web.whatsapp.com/'
# responce=requests.get(url)
# if responce.status_code == 200:
#     soup=BeautifulSoup(responce.text,"html.parser")
#     for link in soup.find_all('a'):
#         href=link.get('href')
#         if href:
#             print(href)


# import requests
# from bs4 import BeautifulSoup
# url='https://web.whatsapp.com/'
# responce=requests.get(url)
# if responce.status_code == 200:
#     soup=BeautifulSoup(responce.text,"html.parser")
#     for link in soup.find_all('a'):
#         href=link.get('href')
#         if href:
#             print(href)


# import requests
# from bs4 import BeautifulSoup
# url='https://web.whatsapp.com/'
# responce=requests.get(url)
# if responce.status_code == 200:
#     soup=BeautifulSoup(responce.text,"html.parser")
#     for link in soup.find_all('a'):
#         href=link.get('href')
#         if href:
#             print(href)

# import requests
# from bs4 import BeautifulSoup
# url='https://web.whatsapp.com/'
# responce=requests.get(url)
# if responce.status_code == 200:
#     soup=BeautifulSoup(responce.text,"html.parser")
#     for link in soup.find_all('a'):
#         href=link.get('href')
#         if href:
#             print(href)



# import requests
# from bs4 import BeautifulSoup
# url='https://web.whatsapp.com/'
# responce=requests.get(url)
# if responce.status_code==200:
#     soup=BeautifulSoup(responce.text,"html.parser")
#     for link in soup.find_all('a'):
#         href=link.get('href')
#         if href:
#             print(href)



# # def divide_number():
#     try:
#         num1=float(input("enter your first number"))
#         num2=float(input("enter your second number"))
#         result=num1/num2
#         print(f"result of {num1}/{num2}={result}")
#     except ZeroDivisionError:
#         print("error:cannot divide by zero")
#     except ValueError:
#         print("error please enter valid number")
#     finally:
#         print("division operation completed")

# divide_number()


def divide_number():
      
    try: 
       num1=float(input("entre your first number:"))
       num2=float(input("enter your second number"))
       result=num1/num2
       print(f"the result is {num1}/{num2}={result}")
    except ZeroDivisionError:
       print("this number is invaild")
    except ValueError:
       print("please enter correct value")
    finally:
       print("division opration completed")

divide_number()

