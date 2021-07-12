import requests
import pandas
from bs4 import BeautifulSoup


         

header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
ans=requests.get('https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=3008&RPT_CAT=M%5FYEAR', headers=header)
ans.encoding='utf-8'
#ans.text

soup=BeautifulSoup(ans.text,'lxml')
data=soup.select_one('#divDetail')

dfs=pandas.read_html(data.prettify())
#len(dfs)
print(dfs[0])




        
        
    

   



