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

# print download speed 
print("DOWNLOAD SPEED")
print(f"Your download speed: {download_speed / 1024 /1024: 3f} Mbps")

print("")

# print upload speed 
print("UPLOAD SPEED")
print(f"Your upload speed: {upload_speed / 1024 /1024: 3f} Mbps")

# print date and time to console
print("")
print("Date and Time completed:", time_and_date)
