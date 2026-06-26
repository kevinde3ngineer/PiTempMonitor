# kevinde3ngineer Temp_Notifier Python Script

import subprocess
import time
from datetime import datetime

def get_pi_temp():
    try:
        result = subprocess.run(
            ["vcgencmd", "measure_temp"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error reading temperature: {e}"

while True:
    temp = get_pi_temp()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Pi temp: {temp}", flush=True)
    time.sleep(10)