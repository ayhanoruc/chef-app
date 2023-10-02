from selenium import webdriver
from selenium.webdriver.common.by import By
from selectolax.parser import HTMLParser
from selenium.webdriver.firefox.options import Options

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

