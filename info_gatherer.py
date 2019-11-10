import os

start_pong = 'pgzrun pong_zero.py'

print('Do you want to play pong? (Y/n)')
answer = str(input())

if answer == ' ' or answer == 'y' or answer == 'Y':

    os.system(start_pong)

else:

    print('Have a good day :)')
