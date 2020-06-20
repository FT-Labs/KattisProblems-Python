time = input().split(" ")
hour = int(time[0])
minute = int(time[1])

alarmminute = minute-45
if alarmminute>=0:
    print(f"{hour} {alarmminute}")
else:
    if hour==0:
        print(f"23 {60+alarmminute}")
    else:
        print(f"{hour-1} {60+alarmminute}")
