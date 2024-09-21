import requests
import selectorlib
import time


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
    with open('data.txt', 'a')as file:
        content = file.write(extracted+'\n')
    return content


if __name__ == "__main__":
        source = scrape(url)
        extracted = extract(source)
        time_now = now()
        print(extracted)
        write(time_now + ',' + extracted)





