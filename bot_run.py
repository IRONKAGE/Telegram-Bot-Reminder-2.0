import time
import runpy

print('BOT Reminder RUN')

while True:
    runpy.run_module(mod_name='bot')
    time.sleep(60)