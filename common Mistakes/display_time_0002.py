
import time
from datetime import datetime

## 이렇게 하면 처음 호출한 시간이 계속 출력된다.
def display_time(time=datetime.now()):
    print(time.strftime('%B %d, %Y %H:%M:%S'))

####display_time()
####time.sleep(1)
####display_time()
####time.sleep(1)
####display_time()

## default argument에 대한 해석은 이렇게 하는 것이 정석일지도.
def display_time_each(time=None):
    if time is None:
        time = datetime.now()
    print(time.strftime('%B %d, %Y %H:%M:%S'))

display_time_each()
time.sleep(1)
display_time_each()
time.sleep(1)
display_time_each()
