import time
import datetime

# 返回程序运行的时间。
print(time.clock())
time.sleep(2)
print(time.clock())

# 返回时间戳
print(time.time())

print(time.gmtime(time.time()))
# time.struct_time(tm_year=2022, tm_mon=6, tm_mday=9, tm_hour=6, tm_min=48, tm_sec=37, tm_wday=3, tm_yday=160, tm_isdst=0)
print(time.localtime(time.time()))

print(time.asctime(time.localtime()))  # "Thu Jun  9 14:49:49 2022"

print(time.ctime(time.time()))

print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d"))