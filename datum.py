"""
Author : Arda
Date : 6/28/2020
"""

weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

monthFirstDay = [3,6,6,2,4,0,2,5,1,3,6,1]

d,m = [int(x) for x in input().split()]
currentDay = (monthFirstDay[m-1]+d-1)%7

print(weekDays[currentDay])