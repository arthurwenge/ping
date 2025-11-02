import time
import urllib.request
import urllib.error

CHECK_URL = "https://www.google.com"
CHECK_INTERVAL_SECONDS = 60

def is_online(url: str) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=5):
            return True
    except urllib.error.URLError:
        return False

if __name__ == "__main__":
    print("Starting the internet connection monitor. Press Ctrl+C to stop.")
    while True:
        online = is_online(CHECK_URL)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        status = "Connected ✅" if online else "Disconnected ❌"
        print(f"[{timestamp}] {status}")
        time.sleep(CHECK_INTERVAL_SECONDS)
