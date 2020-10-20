#requests+xpath
from lxml import etree
import requests
import warnings
import unicodedata

warnings.filterwarnings("ignore")#由于requests获取网页源代码采用verify=False，需要忽略警告
headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}


needsave = [] 

def get_urls(URL):
    Html=requests.get(URL,headers=headers,verify=False)
    Html.encoding = 'utf-8'
    HTML=etree.HTML(Html.text)
    urls=HTML.xpath("//ul[@class='chapter']//a/@href")
    names=HTML.xpath("//ul[@class='chapter']//a/text()")
    return names,urls


def get_items(url):
    html=requests.get(url,headers=headers,verify=False)
    html.encoding = 'utf-8'
    html=etree.HTML(html.text)
    #resultstitle=html.xpath("//div[@id='nr_title']/text()")
    resultsbody=html.xpath("//div[@class='nr_nr']//div[1]/text()")
    items=str(resultsbody).replace('\\r\\n','').replace('\', \'','').replace('\\r\\n\\u3000\\u3000','').replace('\\u3000\\u3000','').replace('\\xa0\\xa0\\xa0\\xa0','').replace('\\r\\n\\r\\n','\n\n').replace('[\'','').replace('\']','')+'\n'*2
    #items=str(resultsbody).replace('\\u3000\\u3000','')+'\n'*2
    #items=unicodedata.normalize('NFKC', str(resultsbody))
    #response = etree.HTML(text=str(resultsbody))
    #print(response.xpath('string(.)'))
    return items

def save_to_file(items):
    with open ("xiaoshuo2.txt",'a',encoding='utf-8') as file:
        for key,value in items:
            file.write(key+'\n')
            file.write(value+'\n')
    #items.clear 
    
def main(URL):
    names,urls=get_urls(URL)
    for name,url in zip(names, urls):
        print(name)
        #save_to_file(name+'\n'*2)
        print(url)
        detail=get_items(url)
        #print(detail)
        #save_to_file(detail)
        print('get!-------------')
        needsave.append((name,detail))
if __name__ == '__main__':
    URL='https://m.jinshulou.net/mulu/125921.html'
    main(URL)
    #i=2
    # while i<49:
    #     URL="https://m.jinshulou.net/mulu/2_{0}.html".format(i) 
    #     i+=1
    #     print(URL)
    #     main(URL)
    save_to_file(needsave)
    print('Done!')