import time
import datetime

current_time = time.time()
date = datetime.datetime.now()

print(f"Seconds since January 1, 1970: {current_time:,.4f}, {current_time:,.2e} in scientific notation")
print(date.strftime("%b"), date.strftime("%d"), date.strftime("%Y"))