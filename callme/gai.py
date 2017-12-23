import os, django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gainers.settings")


from bs4 import BeautifulSoup
import requests
import time
from selenium.webdriver.chrome.options import Options
### TOR crawling

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
# CHROMEDRIVER_PATH = "./chromedriver.exe"
#

GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')




def removeDoubleSpace(st):
    mystring = str(st).strip()  # the while loop will leave a trailing space,
    while '  ' in mystring:
        mystring = mystring.replace('  ', ' ')
    x = str(re.sub(r"\t", "", str(mystring)))
    x1 = str(re.sub(r"\n", "", str(x)))
    return x1
def mainCategory(url1, firebase):


    for i in range(1, 11):
        firebase.delete('/Ticker', i)
        pass

    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    # browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)=
    browser.get(str(url1))
    soup = BeautifulSoup((browser.page_source).encode('utf-8'), 'html.parser')



    categoryList = soup.findAll('tr', attrs={'valign': 'top'})
    # print(len(categoryList))
    dic_list = []
    num = 0


    # firebase = firebase.FirebaseApplication('https://stockapp-238b6.firebaseio.com/', None)
    # result = firebase.get('/users', None)
    # print (result)
    for category in categoryList:
        lists = category.findAll('td')
        count = 0
        # print("Lists" , len(lists))
        for l in lists:

                # print(num)
                if count == 1:
                    Ticker = removeDoubleSpace(str(l.text))

                    # print("Ticker" , Ticker)
                elif count == 2:
                    Company = removeDoubleSpace(str(l.text))
                    # print("Company" , Company)
                elif count == 8:
                    Price = removeDoubleSpace(str(l.text))
                    # print("Price" , Price)
                elif count == 9:
                    Change = removeDoubleSpace(str(l.text))
                    # print("Change" , Change)
                elif count == 10:
                    Volume = removeDoubleSpace(str(l.text))
                    # print("Volume" , Volume)
                count = count + 1
        if num > 0 and num < 11:

            dic = { Ticker ,Company, Price, Change,Volume }
            abs = Ticker+","+Company+","+Price+","+Change+","+Volume;
            dic_list.append(dic)
            print(dic)

            result = firebase.put('/Ticker', num, abs)
            print(result)
        num = num + 1
    return dic_list

# if __name__ == '__main__':
def main():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://stockapp-238b6.firebaseio.com/', None)
    mainCategory('https://finviz.com/screener.ashx?v=110&s=ta_toplosers', firebase)

main()