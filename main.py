import requests
import selectorlib
import time
import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

url = 'https://programmer100.pythonanywhere.com/'


def now():
    content = time.strftime('%y-%m-%d-%H-%M-%S')
    return content



def scrape(url):
    content = requests.get(url)
    source = content.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('temp.yaml')
    value = extractor.extract(source)['temp']
    return value

def write(extracted):
    cursor = connection.cursor()
    extracted = extracted.split(',')
    extract = [item.strip() for item in extracted]
    date,temperature = extract
    cursor.execute("INSERT INTO temp Values(?,?)", (date,temperature))
    connection.commit()


source = scrape(url)
extracted = extract(source)
time_now = now()
extractor = time_now + ',' + extracted
write(extractor)



