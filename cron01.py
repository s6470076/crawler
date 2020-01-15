#리눅스에서만 가능함

#pip install apscheduler

from apscheduler.schedulers.blocking import BlockingScheduler
import time

def exec_interval():#일정 시간으로 수행
    print("hellow world")

def exec_cron():
    str = time.strftime('%c', time.localtime(time.time()))
    print("cron:", str)

sched = BlockingScheduler()
#5ch rksrurdmfh exec-interval()함수 호출하기
sched.add_job(exec_interval,'interval', seconds=60)


#예약하기 (매 시간 10초 30초일 경유 구동)
sched.add_job(exec_cron,'cron', minute="*",second="10, 30")
sched.start()