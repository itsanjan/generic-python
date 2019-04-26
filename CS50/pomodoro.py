import time

start_time = time.time()
break_time = input("length of break: ")
work_time = input("length of work time: ")
count_tomatoes = 2

print(int(start_time))
print(int(start_time) + int(work_time))

while 1:

    if int(start_time) + int(work_time) <= time.time():
        print("You need a break")
        if int(start_time) + int(work_time) <= time.time(): #Alt1
            print("You need a break")
            count -=1
        #Alt 2
        # time.sleep(break_time)
    if count == 0:
        break
