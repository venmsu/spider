'''
 * @Author: ven 
 * @Date: 2018-01-28 18:09:27 
 * @Last Modified by:   ven 
 * @Last Modified time: 2018-01-28 18:09:27 
 '''
# 此次爬虫介绍天猫笔记本电脑销量前60的商品的爬取，
# 抓取内容：商品名称，商品价格，商品链接，店铺名称，店铺链接
# 爬取的时候之前返回了多次302，301  但是html网页还是被爬取下来了

# --------------topgood-------------------------------
# 抓取的首页：
        start_urls = ['https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.4b3df937tMXU1S&cat=50024399&sort=d&style=g&active=1&industryCatId=50024399&theme=663']

# start_urls   ---定义需要访问的首页网址
# parse函数    ---爬虫必须定义的一个函数，scrapy自动爬取首页的html 返回response到parse（解析）函数，在该函数中解析出自己要的数据，并可通过
#                 yield scrapy.Request()返回新的request对象
# parse_detail()   ---可自定义解析函数，通过callback 把response返回到自定义解析函数中进行解析。
# extract()   ---序列化字符串并返回list
# extract_first()   ---提取第一个
# strip()  ---去掉字符串首尾的指定字符，默认空格

# ------------item.py----------------------------
     name = scrapy.Field()  --记录需要爬取内容的对象

# ------------setting.py----------------------------
# BOT_NAME   ---项目名称
# DEFAULT_REQUEST_HEADERS   ---默认请求头
# DEPTH_LIMIT   ---爬取网页的深度，默认零
# ITEM_PIPELINES   ---保存项目中启用的pipeline及其顺序的字典。该字典默认为空，值(value)任意。 不过值(value)习惯设定在0-1000范围内。

# LOG_ENABLED   ---是否启动logging
# LOG_ENCODING   ---logging的编码
# LOG_FILE   ---日志文件的文件名
# LOG_LEVEL   ---日志记录的级别   （CRITICAL、 ERROR、WARNING、INFO、DEBUG）
#                                （关键，     错误， 警告，    信息，调试）
# LOG_STDOUT   --- 默认: False
#               如果为 True ，进程所有的标准输出(及错误)将会被重定向到log中。
#               例如， 执行 print 'hello' ，其将会在Scrapy log中显示。
# RANDOMIZE_DOWNLOAD_DELAY   ---默认为True，在相同网站获取数据时随机暂停
#                               DOWNLOAD_DELAY  默认为0
# ROBOTSTXT_OBEY  默认False，是否遵守robots.txt策咯
# FEED_FORMAT   --- 设置数据保存的形式
# FEED_URI   --- 保存数据的路径和文件名