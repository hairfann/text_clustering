# %%
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

import os
import sys
import random

import pandas as pd

# def crawl_by_demand(url, css_selector):
#     PATH = r"D:\misc\chromedriver-win64\chromedriver.exe"

#     driver = webdriver.Chrome(PATH)
#     driver.maximize_window()
#     driver.get(url)
#     sleep(random.uniform(1, 2))

#     category = driver.find_elements(By.CSS_SELECTOR, css_selector)
#     category = [c for c in category]
#     category = [c.get_attribute("href") for c in category]



# OUTPUT: pandas dataframe
def load_json(file_path):
    import json
    with open(file_path) as f:
        data = json.load(f)
        df = pd.DataFrame(data)
    return df
    

def crawl_(url:str, column:pd.Series, type:str, instance:str):  
    import time
    PATH = r"D:\misc\chromedriver-win64\chromedriver.exe"

    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    driver.get(url)
    tmp = ''

    for e, url in enumerate(column):
        try:
            if column[e] != 'Error':
                continue
            driver.get(url)
            time.sleep(3.14)
            if type == 'class':
                articles = driver.find_elements(By.CLASS_NAME, instance)
            elif type == 'css':
                articles = driver.find_elements(By.CSS_SELECTOR, instance)
            for a in articles:
                tmp += a.text + '\n'
            column[e] = str(tmp)
            print(f'Finished no.{e+1} article')
            tmp = ''
        except:
            print(f'Error at {e+1}')
            column[e] = 'Error'
            continue
    return column