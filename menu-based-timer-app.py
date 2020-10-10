import sys
import time

print('''
- Set a Start Time (0)
- Get Time Elasped Since Start Time (1)
- Get Current time (2)
- Exit (3) 
''')

start_time = time.time()
elapsed_time = 0.0

while True:
    text = input("") 
    if (text == '0'):
        start_time = time.time()
        print('start_time = '+ str(start_time))
    if (text == '1'):
        elapsed_time = time.time() - start_time
        print('Time Since Start Time:' + str(elapsed_time))
    if (text == '2'):
        cur_time = time.time()
        print(cur_time)
    if (text == '3'):
        sys.exit('exiting app')

