# -*- coding: utf-8 -*-

# Scrapy settings for tianmao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tianmao'

SPIDER_MODULES = ['tianmao.spiders']
NEWSPIDER_MODULE = 'tianmao.spiders'

LOG_FILE = 'topgood.log'
LOG_STDOUT=True
DEPTH_LIMIT = 2
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"

# Output .csv  
FEED_URI = u'goods.csv'  
FEED_FORMAT = 'CSV' 
DOWNLOAD_DELAY = 5
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# 禁止cookies,防止被ban  
#COOKIES_ENABLED = False 
#REDIRECT_ENABLED = False
#HTTPERROR_ALLOWED_CODES = [301, 302]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
   'Accept-Encoding': 'gzip, deflate, br',
   'Accept-Language': 'zh-CN,zh;q=0.8',
   "Cookie":"l=AvT0KMp6GsKXLRM0OAHpxea0RLhmJBi3; cna=Ap6HEVfOxycCAWVEhwp4s0Oe; UM_distinctid=15fd2e215be703-084f2010545bce-5d4e211f-1fa400-15fd2e215bf52c; x=__ll%3D-1%26_ato%3D0; enc=2p%2FZNtuaAhZkRg6F8UaCTyDktZbQViJWH3MlaBroJ296diAU7FKlkKq2cjW7suD8dM146OGn%2B0CRubQaYmShOg%3D%3D; _m_h5_tk=1b0aeabeb50a2ccf3b3d997a5ee71694_1516967061506; _m_h5_tk_enc=9f3d4341c8a1d69a62b3860cd0e09292; swfstore=246091; pnm_cku822=098%23E1hvYpvUvbpvUvCkvvvvvjiPPLSvsjlWPFd9sjYHPmPwtjD8P25pgjr2P2LUAjDniQhvCvvv9UUtvpvhvvvvvvGCvvpvvPMMvphvC9v9vvCvpvyCvhQvaypvCANvqU0HKfE9Za2IAXZTKFEw9b7gQfut8v2OibmlHs9lBuV918p7regJlw03ICeZfvDr1RCl5iX1cwe9sbvXHkx%2F1RCliC4AKphv8vvvvvCvpvvvvvv2ThCvCmGvvUnvphvpgvvv96CvpCvOvvm2phCvhCkEvpvVmvvC9jxvuphvmvvv9bC0hv5B; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTdfDY2Rw%2BSeg%3D%3D&lng=zh_CN&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&existShop=false&cookie21=VFC%2FuZ9ajCbF99I1vYLJ2A%3D%3D&tag=8&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0; uc3=sg2=BdS4KP52QYTu8mQXYXiMalWPozai3rwld9Ryym87ve8%3D&nk2=F5Qqb4TejT6f&id2=VADebR8oAI6s&vt3=F8dBzLliVsMIitUL%2FFA%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; tracknick=tb_751440; _l_g_=Ug%3D%3D; unb=716965397; lgc=tb_751440; cookie1=W8GPxnspmeNCFqfrQSWyWBDNvnfmLqSdyTqKsx42uC8%3D; login=true; cookie17=VADebR8oAI6s; cookie2=1a1d8cedd271f0d26f7e1205d3d20f36; _nk_=tb_751440; uss=BdTqhMKPvl56JKlK4HFLCwEjo9myoejcA7lSAuMxVWL9ajIHPCkMxPNiCm8%3D; sg=076; t=e7d1bed12fac3b8c6712e12d6f37a6e0; _tb_token_=5d6f73eb08333; cq=ccp%3D0; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; whl=-1%260%260%260; isg=BAMDdvutXQbjWhKf_5G4YphmkscBbJ2-M0vIETXg1WLZ9CMWv0gnCuFuaoa61O-y",
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tianmao.middlewares.TianmaoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tianmao.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'tianmao.pipelines.TianmaoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
