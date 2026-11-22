# настенные часы
time_mins = int(input())
start_hours = int(input())
start_mins = int(input())

total_mins = start_hours * 60 + start_mins + time_mins

hours = (total_mins // 60) % 24
minutes = total_mins % 60

print(hours, minutes)