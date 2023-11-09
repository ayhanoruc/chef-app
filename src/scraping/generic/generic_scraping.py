from selenium import webdriver
from selenium.webdriver.common.by import By
from selectolax.parser import HTMLParser
from selenium.webdriver.firefox.options import Options
import pandas as pd 
from typing import List
import os 
import re
import json 

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


def read_xlsx(file_path:str)->pd.DataFrame:
    df = pd.read_excel(file_path, header=0)
    print(df.info())
    return df 



        
def record_to_json(path:str):
    """
    Converts a given record file in .xlsx format to JSON format.

    Parameters:
    - path (str): The path to the record file.

    Returns:
    None
    """
    json_path = os.path.splitext(path)[0]+".json"
    data = read_xlsx(path).to_json(json_path,orient="records", indent=4) # here indent=4 makes it prettier
    print(f"Data saved to {json_path}")

    
def read_json(path:str):
    with open(path, 'r') as f:
        data = json.load(f)
        
    return data 

def image_url_parser(recipe_card:str)->str:
    
    pattern = r'https[^"]+\.jpg'
    print(recipe_card)
    match = re.findall(pattern, recipe_card)
    if match:
        return match[0]
    
    return None 




# EXAMPLE USAGE OF URL PARSER FUNCS.
#path = r'C:\Users\ayhan\Desktop\ChefApp\artifacts\recipes\breakfast\breakfast-cereals.json'
"""json_text = read_json(path)

card_info = json_text[2]["recipe_card"] 
url = json_text[2]["recipe_card-href"] # recipe url
print(image_url_parser(card_info)) # recipe image
print(url)"""

features = ["recipe_card","recipe_card-href","recipe_tags","recipe_name",
"recipe_servings","recipe_prep_time","recipe_cook_time","recipe_total_time","recipe_nutrition","recipe_ingredients","recipe_directions"]




recipes_dir = r"C:\Users\ayhan\Desktop\ChefApp\artifacts\recipes"

categories = os.listdir(recipes_dir)

"""for category in categories:

    file_names: List = [name for name in  os.listdir(os.path.join(recipes_dir,category)) if name.endswith(".xlsx")]
    print(category,"/////////////////////")
    for file in file_names:
        print(file)
        path = os.path.join(recipes_dir,category,file)
        record_to_json(path)"""




