import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from colorama import Fore,Back,init,Style
import logging


class Info():
    def __init__(self,groupDf):
        # self.codeDict={}
        # for index,row in group:
        #     addElement={row['Name']:row['Code']}
        #     self.codeDict.update(addElement)
        self.infoDf= groupDf
        self.headers={'Host': 'finance.vietstock.vn',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
                      }

    
    def CollectInfo(self):
        listPrice=[]
        listChangeValue=[]
        listChangePercent=[]
        listColor=[]
        try:
            for index,row in self.infoDf.iterrows():
                code= row['Code']
                response= requests.get(code,headers=self.headers)
                soup= BeautifulSoup(response.content,'lxml')
                price= soup.find('h2',id='stockprice').find('span').text
                #2 element value and percent in pricechange
                priceChange= soup.find('div',id='stockchange').find_all('span')
                changeValue= priceChange[0].text
                if changeValue=='':changeValue='0'
                changePercent= priceChange[1].text
                color= priceChange[0]['class'][0]
                listPrice.append(price)
                listChangeValue.append(changeValue)
                listChangePercent.append(changePercent)
                listColor.append(color)
            self.infoDf['Price']=listPrice
            self.infoDf['Change']=listChangeValue
            self.infoDf['Percent']=listChangePercent
            self.infoDf['Color']=listColor
            return True
        except requests.exceptions.ConnectionError:
            logging.warn('Request timeout may be connection problems')
            return False

    def ShowInfo(self):
        init()
        for index,row in self.infoDf.iterrows():
            normalColor= Style.RESET_ALL
            if 'green' in row['Color']:
                color= Back.GREEN+Fore.BLACK
            elif 'orange' in row['Color']:
                color= Back.LIGHTWHITE_EX+Fore.BLACK
            elif 'purple' in row['Color']:
                color= Back.MAGENTA+Fore.BLACK
            elif 'red' in row['Color']:
                color= Back.RED+Fore.BLACK
            else:
                color= Back.CYAN+Fore.BLACK
            print(normalColor,'{:>6}'.format(row['Name']+'  '),end='')
            print(normalColor,'\t',end='')
            print(color,'{:>10}'.format(row['Price']+'  '),end='')
            print(normalColor,'\t',end='')
            print(color,'{:>10}'.format(row['Change']+'  '),end='')
            print(normalColor,'\t',end='')
            print(color,'{:>10}'.format(row['Percent']+'  '),end='')
            print(normalColor)
        print(Style.RESET_ALL)
        
            

            








