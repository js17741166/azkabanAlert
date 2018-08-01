# -*- encoding:utf8 -*-
'''
@author: KG
@version: 2018-08-01
'''
import datetime, time

# 定义的日期的格式，可以自己改一下，比如改成"$Y年$m月$d日"
format_date = "%Y-%m-%d"
format_datetime = "%Y-%m-%d %H:%M:%S"


def getCurrentDate():
    '''
            获取当前日期：2013-09-10这样的日期字符串
    '''
    return time.strftime(format_date, time.localtime(time.time()))


def getCurrentDateTime():
    '''
            获取当前时间：2013-09-10 11:22:11这样的时间年月日时分秒字符串
    '''
    return time.strftime(format_datetime, time.localtime(time.time()))


def getCurrentHour():
    '''
            获取当前时间的小时数，比如如果当前是下午16时，则返回16
    '''
    currentDateTime = getCurrentDateTime()
    return currentDateTime[-8:-6]


def getDateElements(sdate):
    '''
            输入日期字符串，返回一个结构体组，包含了日期各个分量
            输入：2013-09-10或者2013-09-10 22:11:22
            返回：time.struct_time(tm_year=2013, tm_mon=4, tm_mday=1, tm_hour=21, tm_min=22, tm_sec=33, tm_wday=0, tm_yday=91, tm_isdst=-1)
    '''
    dformat = ""
    if judgeDateFormat(sdate) == 0:
        return None
    elif judgeDateFormat(sdate) == 1:
        dformat = format_date
    elif judgeDateFormat(sdate) == 2:
        dformat = format_datetime
    sdate = time.strptime(sdate, dformat)
    return sdate


def getDateToNumber(date1):
    '''
            将日期字符串中的减号冒号去掉:
            输入：2013-04-05，返回20130405
            输入：2013-04-05 22:11:23，返回20130405221123
    '''
    return date1.replace("-", "").replace(":", "").replace("", "")


def judgeDateFormat(datestr):
    '''
            判断日期的格式，如果是"%Y-%m-%d"格式则返回1，如果是"%Y-%m-%d %H:%M:%S"则返回2，否则返回0
            参数 datestr:日期字符串
    '''
    try:
        datetime.datetime.strptime(datestr, format_date)
        return 1
    except:
        pass

    try:
        datetime.datetime.strptime(datestr, format_datetime)
        return 2
    except:
        pass

    return 0


def minusTwoDate(date1, date2):
    '''
            将两个日期相减，获取相减后的datetime.timedelta对象
            对结果可以直接访问其属性days、seconds、microseconds
    '''
    if judgeDateFormat(date1) == 0 or judgeDateFormat(date2) == 0:
        return None
    d1Elements = getDateElements(date1)
    d2Elements = getDateElements(date2)
    if not d1Elements or not d2Elements:
        return None
    d1 = datetime.datetime(d1Elements.tm_year, d1Elements.tm_mon, d1Elements.tm_mday, d1Elements.tm_hour,
                           d1Elements.tm_min, d1Elements.tm_sec)
    d2 = datetime.datetime(d2Elements.tm_year, d2Elements.tm_mon, d2Elements.tm_mday, d2Elements.tm_hour,
                           d2Elements.tm_min, d2Elements.tm_sec)
    return d1 - d2


def dateAddInDays(date1, addcount):
    '''
            日期加上或者减去一个数字，返回一个新的日期
            参数date1：要计算的日期
            参数addcount：要增加或者减去的数字，可以为1、2、3、-1、-2、-3，负数表示相减
    '''
    try:
        addtime = datetime.timedelta(days=int(addcount))
        d1Elements = getDateElements(date1)
        d1 = datetime.datetime(d1Elements.tm_year, d1Elements.tm_mon, d1Elements.tm_mday)
        datenew = d1 + addtime
        return datenew.strftime(format_date)
    except Exception as e:
        print e
        return Nonedef


def dateAddInMinutes(date1, addcount):
    '''
            日期加上或者减去一个数字，返回一个新的日期
            参数date1：要计算的日期
            参数addcount：要增加或者减去的数字，可以为1、2、3、-1、-2、-3，负数表示相减
    '''
    try:
        addtime = datetime.timedelta(minutes=int(addcount))
        d1Elements = getDateElements(date1)
        d1 = datetime.datetime(d1Elements.tm_year, d1Elements.tm_mon, d1Elements.tm_mday, d1Elements.tm_hour,
                               d1Elements.tm_min, d1Elements.tm_sec)
        datenew = d1 + addtime
        return datenew.strftime(format_datetime)
        return datenew
    except Exception as e:
        print e
        return None


def is_leap_year(pyear):
    '''
            判断输入的年份是否是闰年
    '''
    try:
        datetime.datetime(pyear, 2, 29)
        return True
    except ValueError:
        return False


def dateDiffInDays(date1, date2):
    '''
            获取两个日期相差的天数，如果date1大于date2，返回正数，否则返回负数
    '''
    minusObj = minusTwoDate(date1, date2)
    try:
        return minusObj.days
    except:
        return None


def dateDiffInSeconds(date1, date2):
    '''
            获取两个日期相差的秒数
    '''
    minusObj = minusTwoDate(date1, date2)
    try:
        return minusObj.days * 24 * 3600 + minusObj.seconds
    except:
        return None


def getWeekOfDate(pdate):
    '''
            获取日期对应的周，输入一个日期，返回一个周数字，范围是0~6、其中0代表周日
    '''
    pdateElements = getDateElements(pdate)

    weekday = int(pdateElements.tm_wday) + 1
    if weekday == 7:
        weekday = 0
    return weekday


def getTimestamp(date1, isSec):
    try:
        timeArray = time.strptime(date1, format_datetime)
        timestamp = time.mktime(timeArray)
        if bool(isSec):
            return long(timestamp)
        else:
            return long(timestamp) * 1000

    except:
        return None

if __name__ == "__main__":
    '''
            一些测试代码
    '''
    # print(datetime.datetime.now())
    # print(datetime.datetime.now() + datetime.timedelta(days=1))
    # print(datetime.datetime.now() + datetime.timedelta(hours=1))
    # print(datetime.datetime.now() + datetime.timedelta(minutes=-1))
    # print(datetime.datetime.now() + datetime.timedelta(seconds=1))
    print (getCurrentDateTime())
    print(dateAddInMinutes(getCurrentDateTime(), -1))
    # print judgeDateFormat("2013-04-01")
    # print judgeDateFormat("2013-04-01 21:22:33")
    # print judgeDateFormat("2013-04-31 21:22:33")
    # print judgeDateFormat("2013-xx")
    # print "--"
    # print datetime.datetime.strptime("2013-04-01", "%Y-%m-%d")
    # print 'elements'
    # print getDateElements("2013-04-01 21:22:33")
    # print 'minus'
    # print minusTwoDate("2013-03-05", "2012-03-07").days
    # print dateDiffInSeconds("2013-03-07 12:22:00", "2013-03-07 10:22:00")
    # print type(getCurrentDate())
    # print getCurrentDateTime()
    # print dateDiffInSeconds(getCurrentDateTime(), "2013-06-17 14:00:00")
    # print getCurrentHour()
    # print dateAddInDays("2013-04-05", -5)
    # print getDateToNumber("2013-04-05")
    # print getDateToNumber("2013-04-05 22:11:33")
    #
    # print getWeekOfDate("2013-10-01")
