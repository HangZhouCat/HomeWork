import requests
import time

url = 'http://xpppp.com/security/validateCodeServlet'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
def Main():
    for i in range(101):
        response = requests.get(url, headers=headers)
        img = response.content
        with open('img/'+ str(i) + '.jpg','ab') as file:
            file.write(img)
            print(i, ':Ok')
        time.sleep(3)

if __name__ == '__main__':
    Main()

