import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://in.puma.com/in/en"
r=requests.get(url)
# # print(r)

soup = BeautifulSoup(r.text, "html")
# print(soup)

# boxes=soup.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")

# # print(boxes)
# # print(len(boxes))

header1=[]
header2=[]  

names=soup.find_all("h3",class_="w-full mobile:text-sm mobile:pr-0 font-bold text-base pr-5 line-clamp-2")

for i in names:
    print(i.text)
    header1.append(i.text)


prices=soup.find_all("span",class_="whitespace-nowrap text-base font-bold override:opacity-100")

for i in prices:
    print(i.text)
    header2.append(i.text)

sales=soup.find_all("h2",class_="mobile:mt-1 text-sm desktop:text-base font-bold")

for i in sales:
    s=i.text
    print("\n")
print("Puma:-",s)

url="https://in.puma.com/in/en"
r=requests.get(url)
# # print(r)

soup = BeautifulSoup(r.text, "html")
sales=soup.find_all("h2",class_="mobile:mt-1 text-sm desktop:text-base font-bold")
for i in sales:
    s=i.text
    print("\n")
print("Puma:-",s)  




df=pd.DataFrame([header1,header2])
df = df.transpose()
# Rename the columns if needed
df.columns = ['Shoes name', 'Prices']
df.to_csv("Puma_Shoes.csv")