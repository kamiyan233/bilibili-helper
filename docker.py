import datetime
import os
import time

from crontab import CronTab

from helper import logger

time_format = "%Y-%m-%d %H:%M:%S"


def stop_me(_signo, _stack):
    logger.info("Docker container has stoped....")
    exit(-1)

def main():

    logger.info("Running bilihelper with docker")
    env = os.environ
    # cron_signin = '0 7 * * *'
    cron_signin = env["CRON_SIGNIN"]
    cron = CronTab(cron_signin, loop=True, random_seconds=True)

    def next_run_time():
        nt = datetime.datetime.now().strftime(time_format)
        delayt = cron.next(default_utc=False)
        nextrun = datetime.datetime.now() + datetime.timedelta(seconds=delayt)
        nextruntime = nextrun.strftime(time_format)
        logger.info("当前运行时间: {nt}".format(nt=nt))
        logger.info("下次执行时间: {nextruntime}".format(nextruntime=nextruntime))

    def sign():
        logger.info("执行程序中..")
        os.system("python3 helper")

    sign()
    next_run_time()
    while True:
        ct = cron.next(default_utc=False)
        time.sleep(ct)
        sign()
        next_run_time()


if __name__ == '__main__':
    main()
