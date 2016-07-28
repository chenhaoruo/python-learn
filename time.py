import time

while True:
    current_time = time.localtime(time.time())
    print current_time
    if(((current_time.tm_hour == 13) and (current_time.tm_min == 10)
    	and (current_time.tm_sec == 0))):
        print "Hello World"
    time.sleep(1)
