from bs4 import BeautifulSoup
import requests
url= 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url) # yaha pe page ko request bheji ja rahi hai thorugh 'request' and url se use fetch kia jaa raha hai
print(page)
soup = BeautifulSoup(page.text, 'html') #ye beautiful soup help karta hai page ke andar jo bhi likha hai usko niklane mai.
print(soup) #ye pura ka pura html paste kar dega
print(soup.prettify()) #ye bas use format kar dega ki achhe se dikh sake tumhe