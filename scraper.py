import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(1, 12):

    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(0)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_ = "_4rR01T")
    for i in names:
        name = i.text
        Product_name.append(name)
    #print(Product_name)

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
    for i in prices:
        price = i.text
        Prices.append(price)
    #print(Prices)

    descriptions = box.find_all("ul", class_ = "_1xgFaf")
    for i in descriptions:
        description = i.text
        Description.append(description)
    #print(Description)

    reviews = box.find_all("div", class_ = "_3LWZlK")
    for i in reviews:
        review = i.text
        Reviews.append(review)
    #print(Reviews)

    df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews})

df.to_csv("./flipkart.csv")





    # np = soup.find("a", class_ = "_1LKTO3").get("href")
    # cnp = "https://www.flipkart.com"+np
    # print(cnp)
