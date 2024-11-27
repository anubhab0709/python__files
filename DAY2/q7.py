#Create a Python program that greets the user based on the time of day. Use the “time”
# module to get the current hour and offer greetings for Morning, Afternoon, and Evening.

import time as t

current_time = t.localtime()
hour = current_time.tm_hour

if 6 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 18:
    print("Good Afternoon!")
else:
    print("Good Evening!")