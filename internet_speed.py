import speedtest
from datetime import datetime

print("")
print("EXECUTING INTERNET SPEED TEST")
print("Please wait...")
print("")

# get date and time
now = datetime.now()
time_and_date = now.strftime("%d/%m/%Y %H:%M:%S")

# speedtest module
speed_test = speedtest.Speedtest()
download_speed = speed_test.download() 
upload_speed = speed_test.upload() 
ping_outcome = speed_test.results.ping

# pass or fail
download_speed_pass_or_fail = "Download speed is more than 100 Mbps.\nAdvised Verdict: PASS" if download_speed /1024 /1024 >= 100 else "Download speed is less than 100.\nAdvised Verdict: FAIL"
upload_speed_pass_or_fail = "Upload speed is more than 20 Mbps.\nAdvised Verdict: PASS" if upload_speed /1024 /1024 >= 20 else "Upload speed is less than 20.\nAdvised Verdict: FAIL"
ping_pass_or_fail = "Ping time is less than 50ms.\nAdvised Verdict: PASS" if ping_outcome <= 50 else "Ping time is more than 50.\nAdvised Verdict: FAIL"

# print download speed 
print("DOWNLOAD SPEED")
print(f"Your download speed: {download_speed / 1024 /1024: .3f} Mbps")
print(download_speed_pass_or_fail)

print("")

# print upload speed 
print("UPLOAD SPEED")
print(f"Your upload speed: {upload_speed / 1024 /1024: .3f} Mbps")
print(upload_speed_pass_or_fail)

print("")

# print ping time 
print("PING TIME")
print(f"Your ping time: {ping_outcome: .3f}ms")
print(ping_pass_or_fail)

# print date and time to console
print("")
print("Date and Time completed:", time_and_date)
