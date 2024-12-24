import schedule
import time
from databaseAuth import login_auth
from sendRequest import requestSend

schedule.every(1).minutes.do(requestSend)
schedule.every(2).minutes.do(login_auth)
while True:
    schedule.run_pending()
    time.sleep(1)
