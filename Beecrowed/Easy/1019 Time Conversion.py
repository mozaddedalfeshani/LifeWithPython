value = int (input())

value ,hour = value % (60*60), value // 3600
value, mini = value % 60 , value // 60
sec = value

print(f'{hour}:{mini}:{sec}')