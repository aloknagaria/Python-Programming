from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)

soup = BeautifulSoup(page.text, features='html.parser') #yaha par vs code mai alag argument lagta hai thoda sa hi change hain
# print(soup)

# print(soup.find('div')) # jo bhi pehla div encounter hoga usko leke aajayega
# print(soup.find_all('div', class_ = 'col-md-12')) #sare div dhund ke le ayega
# print(soup.find_all('p')) 

# print(soup.find('p', class_ ='lead').text.strip()) # ye hume us p tag ke tagname = lead vale ka text utha ke de dega, without space using the strip function.

print(soup.find_all('th')[0].text.strip())

# or 

th_elements = soup.find_all('th')
first_th_text = th_elements[0].text.strip()
print(first_th_text)
# for th in soup.find_all('th'):
#     print(th.text.strip())