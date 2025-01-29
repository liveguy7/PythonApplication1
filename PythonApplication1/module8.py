import datetime

#print current date and time

def main8():
    now = datetime.datetime.now()
    print("Current date {0}".format(now.strftime('%y-%m-%d')))
    print("Current time {0}".format(now.strftime('%H:%M:%S')))

main8()