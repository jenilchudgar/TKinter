import time
import datetime



while True:
    print(datetime.timedelta(hours=24,minutes=0,seconds=0) - datetime.timedelta(hours=time.localtime().tm_hour,minutes=time.localtime().tm_min,seconds=time.localtime().tm_sec))

    time.sleep(1)