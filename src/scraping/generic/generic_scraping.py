from selenium import webdriver
from selenium.webdriver.common.by import By
from selectolax.parser import HTMLParser
from selenium.webdriver.firefox.options import Options
import pandas as pd 
from typing import List
import os 

URL = "https://medium.com/geekculture/a-complete-12-week-course-to-learn-web-scraping-in-python-for-free-659ed05deb00"
def extract(url):
    options = Options()
    options.headless = True  # headless mode-on
    driver = webdriver.Firefox(options=options)
    
    driver.get(url)
    html = driver.page_source
    driver.close()
    return html

def parse(html,element:str):
    html = HTMLParser(html)
    elements = html.css(element)
    for e in elements:
        print(e.text(strip=True))
    
def main():
    html = extract(URL)
    parse(html,'article')


def read_csv(file_path:str, usecols:List)->None:
    df = pd.read_excel(file_path, usecols=usecols, header=0 )
    df.to_excel(file_path, index=False)
    print("succesfull process!")


path = r"C:\Users\ayhan\Desktop\ChefApp\artifacts\recipes\desserts\desserts-crisps_and_crumbles.xlsx"
features = ["recipe_card","recipe_card-href","recipe_tags","recipe_name",
"recipe_servings","recipe_prep_time","recipe_cook_time","recipe_total_time","recipe_nutrition","recipe_ingredients","recipe_directions"]

read_csv(path,features)

recipes_dir = r"C:\Users\ayhan\Desktop\ChefApp\artifacts\cusine"

categories = os.listdir(recipes_dir)

for category in categories:
    file_names = os.listdir(os.path.join(recipes_dir,category))
    print(category,"/////////////////////")
    for file in file_names:
        print(file)
        path = os.path.join(recipes_dir,category,file)
        read_csv(path,features)
        
    
