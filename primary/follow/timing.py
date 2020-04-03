import urllib.request
import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job


try:
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    @register_job(scheduler, 'cron', day_of_week='mon-fri', hour='18', minute='1', second='0', id='task_time')
    def test_job():
        """
            每天18点01 定时请求接口
        """
        url = 'http://127.0.0.1:8000/send_xls_file/'
        response = urllib.request.urlopen(url)
    register_events(scheduler)
    scheduler.start()
except Exception as e:
    print(e)
    scheduler.shutdown()