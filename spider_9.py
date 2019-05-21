'''
bytes.decode(encoding="utf-8", errors="strict")
str.encode(encoding="utf-8", errors="strict")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
requests.get("XXX", params=kw, headers=headers).content.deocde()
字典传入请求参数及post的data

session类，来实现客户端和服务端的会话保持，主动维护cookie/session等
session = requests.session()
response = session.get(url,headers)

verify=False  忽略证书验证
timeout = 10 超时报错
retrying.retry 重试请求{装饰器}



post地址：勾选perserve log 保存数据
form表单action，对应name为键
寻找js-->寻找点击点-->eventlistener
      -->通过chrome中的searchall 寻找关键字


json.loads(html_str)将json转化为python字典
json.dumps(ret1,ensure_ascii=False,indent=4) 将字典转化json 不ascii并退格4

json.load(f)  当使用类文件对象f时，简化
json.dump(ret1,f,ensure_ascii=False,indent=2)

Xpath重点：
    获取文本
        a/text() 获取a下的文本
        a//text() 获取a下的所有标签的文本
        //a[text()='下一页'] 选择文本为下一页三个字的a标签
    @符号
        a/@href
        //div[contains(@class,'i')]
    //
        在xpath最前面表示从当前html中任意位置开始选择
        li//a 表示的是li下任何一个标签
    限定：//ul[@id="detail-list"]

html = etree.HTML(text)
查看element对象中包含的字符串print(etree.tostring(html).decode())

Selenium和PhantomJS入门 使用无界面浏览器模拟操作获取html或cookie

from pymongo import MongoClient
client = MongoClient(host,port) #建立连接
colelction = client["db"]["collection"] 数据库/集合
操作对象是dict

创建项目 scrapy startproject 项目名
创建爬虫 scrapy genspider spider_name allow_domain
完善爬虫
    start_url,response --> parse -->response.xpath返回的是包含selector对象的列表，需要进一步)extract()/extract_first()得到str值
    数据yield 通过传递给管道
    能够yield 的数据类型，dict，request，Item，None
管道
    开启管道
    开启管道，键:位置，值：小的先执行
运行爬虫
    scrapy crawl baidu
下一页
    scrapy.Request(url,callback,meta,dont_filter)
    dont_filter=True 表示请求过的url地址还会继续被请求
Scrapy shell是一个交互终端  可以调试xpath
parse函数间传递参数
    meta是个字典类型，meta = {"item":item}
    response.meta["item"]
open_spdier/close_spider 爬虫开始/关闭的时候执行一次，只有一次
CrawlSpider
    满足某个条件的url地址，我们才发送给引擎，同时能够指定callback函数
    scrapy genspider –t crawl csdn “csdn.cn”
    follow：连接提取器提取出来的url地址对应的响应是否继续被rules来过滤


logger=logging.getLogger(__name__)日志



'''

from lxml import etree
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
def bdre():

    kw = {'wd': '长城'}

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)

    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print(response.text)

    # 查看响应内容，response.content返回的字节流数据
    print(response.content)

    # 查看完整url地址
    print(response.url)

    # 查看响应头部字符编码
    print(response.encoding)

    # 查看响应码
    print(response.status_code)
if __name__ == '__main__':
    # bdre()
    ua = UserAgent()
    while True:
        print(ua.random)