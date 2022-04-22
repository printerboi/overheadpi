import sys
import schedule, time
from weather import loadWeather

arguments = sys.argv

if arguments[1]:
    if arguments[1] == 'weather':
        schedule.every(5).minutes.do(loadWeather)
    else:
        print("Sorry routine not found...")


while True:
    schedule.run_pending()
    time.sleep(1)