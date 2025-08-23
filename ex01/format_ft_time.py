
from datetime import datetime
import time


# Jnuary 1 1970 = Unix timestap or epoch time

epoch_seconds = time.time()
print(f"Seconds since January 1, 1970: {format(epoch_seconds, ",.4f")} or {format(epoch_seconds, ".2e")} in scientific notation")

current_date = datetime.now()
print(current_date.strftime("%b %d %Y"))