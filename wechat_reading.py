import os
import random
import time

def adb():
    '''连接adb'''
    os.chdir('adb')
    os.system('adb connect 127.0.0.1:62001')

def swipe():
    '''左滑'''
    from_x = random.randint(200, 500)
    from_y = random.randint(200, 800)
    to_x = from_x - 50
    to_y = from_y
    os.system(f'adb shell input swipe {from_x} {from_y} {to_x} {to_y} 200')

def read_min():
    '''一分钟读书'''
    min_before = random.randint(15, 45)
    min_after = 60 - min_before
    swipe()
    time.sleep(min_before)
    print(f'==>您阅读本页用时: {min_before} 秒!')
    swipe()
    time.sleep(min_after)
    print(f'=>>您阅读本页用时: {min_after} 秒!')

def main():
    print('|-----欢迎来到冷哥的读书世界！-----|')
    adb()
    total_time = int(60 * float(input('请输入读书持续时间(小时):')))
    print('阅读开始……')
    for i in range(1, total_time+1):
        read_min()
        print(f'你已经阅读了 {i} / {total_time} 分钟。\n')

    print(f'\n您已经完成了阅读任务，总阅读时间: {total_time} 分钟。')

if __name__ == '__main__':
    main()


