# Speed test
import speedtest

# Declare variable with speedtest
st = speedtest.Speedtest()

start = input("Press Enter to start the speedtest.")
# Measure download speed, upload speed and ping
# Output is in bits -> convert into Megabits
down_speed = st.download() / 1000000
up_speed = st.upload() / 1000000
ping = st.results.ping

# Print results rounded to 2 decimals
print(f"Download speed: {down_speed:.2f} mb/s")
print(f"Upload speed: {up_speed:.2f} mb/s")
print(f"Ping: {ping:.2f}ms")