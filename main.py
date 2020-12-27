# CONTRIBUTED BY AMARTYA PANDEY 27TH DECEMBER 2020
import time

from plyer import notification  # PLYER IS AN EXTERNAL MODULE THAT INTERACTS WITH HARDWARE

if __name__=="__main__":
    while True:
        notification.notify(
            title = "Please blink your eyes for 10 seconds to prevent dryness of eyes",
            message="Your eyes is your everything do take care of it often as you spend hours in fornt of your Computer screen",
            app_icon=r"C:\Users\AMARTYA PANDEY\PycharmProjects\Eye_Caring_Remainder_Application\EYES.ico",
            timeout=15
        )
        time.sleep(60)