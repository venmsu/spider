# -*- coding:utf-8 -*-
import requests
import random
import json
import re
import time
import os
from PIL import Image
import urllib.parse
from config import *
from setting import header, captchaDict, seat
import smtplib
from email.mime.text import MIMEText
from email.header import Header

session = requests.session()
session.verify = False

# 车票输出格式控制
def myAlign(string, length):  
    if u'\u4e00' <= string <= u'\u9fff':
        return string.center(length-len(string))
    else:
        return string.center(length)

# 发送邮件通知
def send_Mail(data, fromstation, tostation):
    msg_from = "784611320@qq.com"
    passwd = "abaerycyyajybcgj"
    msg_to = receiveMail

    subject = "抢票消息通知"
    content= "您好，您抢的{}从{}到{}的车票已经下单，请尽快到12306官网“{}”账号支付！".format(data, fromstation,tostation, coUsername)

    msg = MIMEText(content, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = msg_from
    msg["To"] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com",465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print (e)
    finally:
        s.quit()

# 验证码位置转坐标
def captchaTest(number):
    numList = number.split(",")
    numlocate = ""
    for i in numList:
        numlocate = numlocate + captchaDict[i]+","
    numlocate = numlocate[:-1]
    return numlocate

# 获取站点信息
def get_Stations():
    stationUrl = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.90480"
    header['Referer'] = "https://kyfw.12306.cn/otn/leftTicket/init"
    rstations = requests.get(stationUrl, headers=header)
    stationList = rstations.text.split("'")[1].strip().split("@")[1:]
    stationDict = {}
    for item in stationList:
        temp = item.split("|")
        stationDict[temp[1]]=temp[2]
    
    if os.path.exists("12306station.txt"):
        os.remove("12306station.txt")
    
    with open("12306station.txt","w", encoding='utf8') as f:
        f.write(json.dumps(stationDict, ensure_ascii=False))
    print("全国站点信息更新完成！")

# 车票查询
def query_Ticket():
    
    header["Referer"] = "https://kyfw.12306.cn/otn/leftTicket/init"
    
    with open("12306station.txt", "r", encoding="utf8") as fr:
        stationDict = json.loads(fr.read())

    # query后面的字母变化的  A-Z
    queryUrl = "https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(coDate, stationDict[coFromStation], stationDict[coToStation])
    header['Referer'] = "https://kyfw.12306.cn/otn/leftTicket/init"
    rt = requests.get(queryUrl, headers=header)

    result = rt.json()['data']['result']

    print("< < < < < < "+coFromStation+"=====>"+coToStation+" > > > > > >"+"\n< < < <========余票信息========> > > >:")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("|"+"  车次  "+"|"+"  发车  "+"|"+"  时长  "+"|"+"  日期  "+"|"+"  商务  "+"|"+"  一等  "+"|"+"  二等  "+"|"+"  高软  "+"|"+"  软卧  "+"|"+"  动卧  "+"|"+"  硬卧  "+"|"+"  软座  "+"|"+"  硬座  "+"|"+"  无座  "+"|")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    for item in result:
        # print(item)
        itemList = item.split("|")
        print("|"+myAlign(itemList[3],8)+"|"+myAlign(itemList[8],8)+"|"+myAlign(itemList[10],8)+"|"+myAlign(itemList[13],8)+"|"+myAlign(itemList[31],8)
            +"|"+myAlign(itemList[31],8)+"|"+myAlign(itemList[30],8)+"|"+myAlign(itemList[21],8)+"|"+myAlign(itemList[23],8)+"|"+myAlign(itemList[33],8)
            +"|"+myAlign(itemList[28],8)+"|"+myAlign(itemList[24],8)+"|"+myAlign(itemList[29],8)+"|"+myAlign(itemList[26],8)+"|")
        print("-------------------------------------------------------------------------------------------------------------------------------")
    return result

# 登录账户  
def login():
    
    print("登录中...")
    print("获取验证码...")
    # 验证码的获取与验证
    header["Referer"] = "https://kyfw.12306.cn/otn/login/init"
    captchaData = {           # 验证码使用
        "answer": "",
        "login_site":"E",
        "rand": "sjrand"
    }
    imgUrl = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&"+str(random.random())+str(random.randint(10, 99))
    ri = session.get(imgUrl, headers=header)
    with open("12306.jpg", "wb") as fi:
        fi.write(ri.content)
    img = Image.open("12306.jpg")
    img.show()

    print("-----------------")
    print("|-1-|-2-|-3-|-4-|")
    print("-----------------")
    print("|-5-|-6-|-7-|-8-|")
    captchacode = input("请输入验证码的位置编号，用英文逗号分隔:")
    captchaData['answer'] = captchaTest(captchacode)
    
    captchaUrl = "https://kyfw.12306.cn/passport/captcha/captcha-check"
    rc = session.post(captchaUrl, headers=header, data=captchaData)
    if rc.json()['result_code'] == 4:
        print("\n========\n"+rc.json()['result_message']+"\n========\n")
    else:
        print("\n========\n"+rc.json()['result_message']+"\n========\n")
    
    # 用户登录
    #登录第一步
    lodinData = {          # 登录使用
    "appid":"otn",
    "password":coPassword,
    "username":coUsername
    }
    rl1 = session.post("https://kyfw.12306.cn/passport/web/login", headers=header, data=lodinData)
    try:
        rl1Json = rl1.json()
    except:
        print("第一步错误！")
    if rl1Json["result_code"] == 0:
        print(rl1Json["result_message"])
        rl11 = session.post('https://kyfw.12306.cn/otn/login/userLogin', headers=header, data={"_json_att": ""})
    else:
        print(rl1Json["result_message"])

    # 登录第二步，获取newapptk
    header["Referer"] = "https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin"
    rl2 = session.post("https://kyfw.12306.cn/passport/web/auth/uamtk", headers=header, data={"appid": "otn"})
    try:
        rl2Json = rl2.json()
    except:
        print("第二步错误！")
    if rl2Json['result_code'] == 0:
        print(rl2Json["result_message"])
    else:
        print(rl2Json["result_message"])
    #print(rl2Json["newapptk"])

    # 登录第三步
    rl3 = session.post("https://kyfw.12306.cn/otn/uamauthclient", headers=header, data={"tk":rl2Json["newapptk"]})
    try:
        rl3Json = rl3.json()
    except:
        print("第三步错误！")
    if rl3Json['result_code'] == 0:
        print(rl3Json["result_message"])
    else:
        print(rl3Json["result_message"])
    
    print("登录流程完成...")
    
# 车票购买
def buy_Ticket():
    login()
    while True:
        time.sleep(5)
        result = query_Ticket()
        resultDict = {}
        for item in result:
            itemList = item.split("|")
            resultDict[itemList[3]] = itemList
        if coTraincode in resultDict and resultDict[coTraincode][seat[coSeatType][0]] == "无" or resultDict[coTraincode][seat[coSeatType][0]] == "":
            print("+++++++++++++++++++++++++++++++")
            print("|------没有余票，继续抢票-----|")
            print("+++++++++++++++++++++++++++++++")
            continue
        else:
            print("++++++++++++++++++++++++++++++")
            print("|--所选位置有余票，抢票开始--|")
            print("++++++++++++++++++++++++++++++")
            break
            #print(resultDict[trainCode])
    
    # checkuser
    time.sleep(random.randint(3, 6))
    header["Referer"] = "https://kyfw.12306.cn/otn/leftTicket/init"
    sp0 = session.post("https://kyfw.12306.cn/otn/login/checkUser", headers=header, data={"_json_att": ""})    
    try:
        sp0Json = sp0.json()
    except:
        print("sp0错误")
    if sp0Json["status"] and sp0Json["data"]["flag"]:
        print("sp0成功")
    else:
        print("sp0失败")
        print(sp0Json["data"]["messages"])
        
    # 预定，提交表单信息
    header["Referer"] = "https://kyfw.12306.cn/otn/leftTicket/init"
    sp1Data = {
            "back_train_date":time.strftime("%Y-%m-%d", time.localtime()),
            "purpose_codes":coPuerpose,
            "query_from_station_name":coFromStation,
            "query_to_station_name":coToStation,
            "secretStr":urllib.parse.unquote(resultDict[coTraincode][0]),
            "tour_flag":coTourflag,
            "train_date":coDate,
            "undefined": ""
            }

    sp1 = session.post("https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest", headers=header, data=sp1Data)
    #print(sp1.text)
    #print(sp1.status_code)
    #print(sp1.url)
    sp1Json = sp1.json()
    
    if sp1Json["status"]:
        print("sp1成功")
    else:
        print("sp1失败")
        print(sp1Json["messages"])
    #time.sleep(0.1)
    
    # 获取重要参数globalRepeatSubmitToken和ticketInfoForPassengerForm
    sp2 = session.post("https://kyfw.12306.cn/otn/confirmPassenger/initDc", headers=header, data={"_json_att":""})
    #print(sp2.text)
    submitTokenRe = re.findall(r"var globalRepeatSubmitToken = '.*?'", sp2.text)
    submitToken = submitTokenRe[0].split("'")[1]
    passengerFormRe = re.findall(r"var ticketInfoForPassengerForm={.*?};", sp2.text)
    passengerForm = passengerFormRe[0].split(";")[0].split("m=")[1]
    time.sleep(round(random.uniform(0,1.5), 1))

    # 获取乘客信息
    header['Referer'] = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    sp3 = session.post("https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs", headers=header, data={"REPEAT_SUBMIT_TOKEN":submitToken, "_json_att":""})
    try:
        passengerJson = sp3.json()
    except:
        print("sp3错误")
    if passengerJson["status"]:
        print("sp3成功")
        passenger = passengerJson["data"]["normal_passengers"]
    time.sleep(round(random.uniform(3, 5), 1))

    # 订单信息确认
    checkData = {
        "cancel_flag": 2,
        "bea_level_order_num": "000000000000000000000000000000",
        "oldPassengerStr": coName+",1,"+coId+",1_",
        "passengerTicketStr": seat[coSeatType][1]+",0,"+"1,"+coName+",1,"+coId+","+coPhonenum+",N",
        "randCode":"",
        "REPEAT_SUBMIT_TOKEN":submitToken,
        "tour_flag":coTourflag,
        "whatsSelect":"1"
    }
    header["Referer"] = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    sp4 = session.post("https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo", headers=header, data=checkData)
    try:
        queueJson = sp4.json()
    except:
        print("sp4错误")
    if queueJson["status"]:
        print("sp4成功")
        print("订单确认成功")
    else:
        print(queueJson["messages"])
    #time.sleep(round(random.uniform(0,1.5), 1))

    #获取余票信息
    timeArray = time.strptime(coDate, "%Y-%m-%d")
    timestamp = time.mktime(timeArray)
    time_local = time.localtime(int(timestamp))
    dt = time.strftime("%a %b %d %Y 00:00:00 GMT+0800 ",time_local)+"(中国标准时间)"

    queueData = {
        "_json_att":"",
        "fromStationTelecode":resultDict[coTraincode][6],
        "toStationTelecode":resultDict[coTraincode][7],
        "leftTicket":resultDict[coTraincode][12],
        "purpose_codes":re.findall(r"'purpose_codes':'[0-9]{0,2}',", passengerForm)[0].split("'")[3],
        "REPEAT_SUBMIT_TOKEN": submitToken,
        "seatType":seat[coSeatType][1],
        "stationTrainCode":coTraincode,
        "train_date": dt,
        "train_location":resultDict[coTraincode][15],
        "train_no":resultDict[coTraincode][2]
    }
    # print(queueData)
    header["Referer"] = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    sp5 = session.post("https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount", headers=header, data=queueData)
    try:
        checkJson = sp5.json()
    except:
        print("sp5错误")
    if checkJson["status"]:
        print("订单验证成功")
    else:
        print(checkJson["messages"])
        try:
            print(checkJson["data"]["errMsg"])
            print(checkJson["messages"])
        except:
            print(checkJson["messages"])
    time.sleep(round(random.uniform(4,6), 1))

    # 座位确认
    confirmData = {
        "_json_att":"",
        "choose_seats":coSeat,
        "dwAll":"N",
        "key_check_isChange":re.findall(r"'key_check_isChange':'.*?',", passengerForm)[0].split("'")[3],
        "leftTicketStr":resultDict[coTraincode][12],
        "oldPassengerStr":coName+",1,"+coId+",1_",
        "passengerTicketStr":seat[coSeatType][1]+",0,"+"1,"+coName+",1,"+coId+","+coPhonenum+",N",
        "purpose_codes":re.findall(r"'purpose_codes':'[0-9]{0,2}',", passengerForm)[0].split("'")[3],
        "randCode":"",
        "REPEAT_SUBMIT_TOKEN":submitToken,
        "roomType":"00",
        "seatDetailType":"000",
        "train_location":resultDict[coTraincode][15]
    }
    sp6 = session.post("https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue", headers=header, data=confirmData)
    try:
        sp6Json = sp6.json()  
    except:
        print("sp6错误！")
    if sp6Json["data"]["submitStatus"]:
        print("座位选择成功")
    else:
        print(sp6Json["data"]["errMsg"])
    #time.sleep(round(random.uniform(0,1), 1))

    #  订单下单状况
    header["Referer"]="https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    trynum = 0
    orderId = ""
    while True:
        sp7 = session.get("https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?random={}&tourFlag={}&_json_att=&REPEAT_SUBMIT_TOKEN={}".format(str(int(time.time()*1000)), coTourflag, submitToken), headers=header)
        try:
            sp7Json = sp7.json()
        except:
            print("sp7错误")
        if sp7Json["data"]["waitTime"] <=0 and sp7Json["data"]["waitCount"] ==0:
            print("下单成功！")
            orderId = sp7Json["data"]["orderId"]
            break
        else:
            trynum += 1
            print(sp7Json)
            print("继续确认下单...")
            time.sleep(random.uniform(0,1))
            if trynum >=3:
                print("还是失败")
                break
    
    # 结果确认
    header["Referer"] = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    resultData = {
        "_json_att":"",
        "orderSequence_no":orderId,
        "REPEAT_SUBMIT_TOKEN":submitToken
    }
    sp8 = session.post("https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue", headers=header, data=resultData)
    try:
        sp8Json = sp8.json()
    except:
        print("sp8错误")
    if sp8Json["status"] and sp8Json["data"]["submitStatus"]:
        print("结果有了")
        send_Mail(coDate,coFromStation, coToStation)
    else:
        print(sp8Json["data"]["errMsg"])
        send_Mail(coDate,coFromStation, coToStation)
