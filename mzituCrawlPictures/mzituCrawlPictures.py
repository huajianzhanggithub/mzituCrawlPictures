import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#针对图片懒加载,用Chrome打开网页,滚动到最后,获得详情页源代码
def get_pageSouce(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    #不显示Chrome
    driver = webdriver.Chrome(chrome_options=chrome_options)
    #显示Chrome
    #driver = webdriver.Chrome()
    #driver.implicitly_wait(10)
    driver.maximize_window()
    try:
        driver.get(url)
        for i in range(100,1000,100):
            #移动到指定的坐标(相对当前的坐标移动)  
            driver.execute_script("window.scrollBy(0, {})".format(i))
            time.sleep(1)
        #time.sleep(2)
    except Exception as e:
        print('发生了{}错误!'.format(e))
    a = driver.page_source
    driver.close()
    return a

urls = ['https://www.mzitu.com/page/{}/'.format(str(i)) for i in range(1,3)]
path = 'D:/Users/Administrator/Pictures/妹子网图片/'

header = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36'
    }

def get_photo(url):
    html = get_pageSouce(url)
    selector = etree.HTML(html)
    photo_urls = selector.xpath('//li/a/img/@src')
    fp = open('妹子图片.txt','w')
    for photo_url in photo_urls:
        fp.write(photo_url + '\n')
    fp.close()

for url in urls:
    get_photo(url)