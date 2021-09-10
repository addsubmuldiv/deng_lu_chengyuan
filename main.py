from selenium import webdriver
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    driver = webdriver.Chrome()
    driver.get("http://10.69.253.12/ac_portal/20190610083017/pc.html?template=20190610083017&tabs=pwd-sms&vlanid=0&url=http://edge.microsoft.com%2fcaptiveportal%2fgenerate_204")
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="password_name"]').send_keys('xxx')   # 城院账号
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="password_pwd"]').send_keys('xxx')   # 城院密码
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="password_submitBtn"]').click()
    time.sleep(1)
    driver.close()

if __name__=='__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', day_of_week='0-6', hour=6, minute=16, misfire_grace_time=3600)
    print('启动')
    scheduler.start()