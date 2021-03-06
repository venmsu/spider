# 12306的参数设置
from fake_useragent import UserAgent
UA = UserAgent()

useragent = UA.random

# 请求头设置
header = {
    "Host": "kyfw.12306.cn",
    "Referer": "https://kyfw.12306.cn/otn/login/init",
    "User-Agent": useragent
        }

# 验证码位置设置
captchaDict = {"1": "35,35","2":"110,35","3":"185,35","4":"265,35",
               "5":"35,110","6":"110,110","7":"185,110","8":"265,110"
               }

# 不同座位对应余票result中的位置，和代号

seat = {
    "高级软卧": [21, "6"],
    "软卧": [23, "4"],
    "软座": [24, "2"],
    "无座": [26, "1"],
    "硬卧": [28, "3"],
    "硬座": [29, "1"],
    "二等座": [30, "O"],
    "一等座": [31, "M"],
    "特等座": [32, "P"],
    "商务座": [32, "9"],
    "动卧": [33, "F"]

}