import lcddriver
import time

display = lcddriver.lcd()


def display_success_lcd():
   print("Writing to display")
   display.display_string("Check-in successful!", 1)
   #display.lcd_display_string("Temperature: " + "{0:.2f}".format(float(firebase.get()), 2)
   time.sleep(2)

   display.lcd_clear()

def display_failure_lcd():
   print("Writing to display")
   display.display_string("Check-in unsuccessful!", 1)
   time.sleep(2)

   display.clear()
try:
   while True:
      print("Writing to display")
      #display.display_string("This is my new", 1)
      #display.display_string("LCD Program!",2)
      #time.sleep(2)
      display_failure_lcd()

except KeyboardInterrupt:
   print("Cleaning up")
   display.clear()
