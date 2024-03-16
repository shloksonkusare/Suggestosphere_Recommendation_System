import requests
from bs4 import BeautifulSoup

# req=requests.get("https://in.puma.com/in/en")

# # soup=BeautifulSoup(req.content,"html.parser")
# # print(soup.get_text())

url="https://in.puma.com/in/en"
r=requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
sales=soup.find_all("h2",class_="mobile:mt-1 text-sm desktop:text-base font-bold")
for i in sales:
    puma=i.text
    print("\n")
print("Puma:-",puma)  

url2="https://www.fila.com/warehouse-sale"
r2=requests.get(url2)
soup = BeautifulSoup(r2.text, "html.parser")
sales2=soup.find("h1",class_="category-title-primary")


# Find the next <p> element after the <h1> element

p_element = sales2.find_next("p")

# Print the text content of the <p> element

# print(p_element.text.strip())


for i in p_element:
    fila=i.text.strip()
    print("\n")
print("Fila:-",fila)  


