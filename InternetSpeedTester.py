# Internet Speed Tester
import speedtest


st = speedtest.Speedtest()

start = input("Press Enter to start")
down_speed = st.download()
up_speed = st.upload()
ping = st.results.ping

print(down_speed)
print(up_speed)
print(ping)