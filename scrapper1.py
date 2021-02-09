from bs4 import BeautifulSoup
import requests
import pandas
url="https://www.adana.co.jp/en/contents/products/na_liquid/detail0"
page_num_liquid=4
scrapped_info_list=[]
for page_num in range(1,page_num_liquid):
    req=requests.get(url + str(page_num)+ '.html')
    content=req.content
    soup=BeautifulSoup(content,'html.parser')
    all_prod=soup.find_all('div',class_="series-box")

    for prod in all_prod:
        prod_dict={}
        prod_dict["Product name"]=prod.find('p',class_='text-title').text
        prod_dict["Product ID"]=prod.find('td',class_='table-cell1').text.split('-')[-1]
        if page_num<3:
            prod_dict["Product description"]=prod.find('td',class_='table-cell2').text
        else:
            prod_dict["Product description"]=prod.find('td',class_='table-cell6').text
        scrapped_info_list.append(prod_dict)

dataframe=pandas.DataFrame(scrapped_info_list)
dataframe.to_csv("adaadditives.csv")
