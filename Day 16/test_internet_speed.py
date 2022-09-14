import speedtest
connection = speedtest.Speedtest()

print("Your connection Download Speed is ",
      connection.download(), 'B')
print("Your connection Upload Speed is ", connection.upload(), 'B')
