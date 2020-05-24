def timeConversion(civilian_time):
    time_split = civilian_time.split(":")    
    if "PM" in time_split[2]:
        time_split[2] = time_split[2].replace("PM",'')
        if int(time_split[0]) != 12:
            time_split[0] = str(int(time_split[0]) + 12)
    if "AM" in time_split[2]:
        time_split[2] = time_split[2].replace("AM",'')
        print(time_split)
        if int(time_split[0]) == 12:
            print(time_split)
            time_split[0] = '00'
    print((":").join(time_split))    
    

timeConversion("12:00:45AM")
timeConversion("01:00:45PM")
timeConversion("02:00:45PM")
timeConversion("03:00:45PM")
timeConversion("04:00:45PM")
timeConversion("05:00:45PM")
timeConversion("06:00:45PM")
timeConversion("07:00:45PM")
timeConversion("08:00:45PM")
timeConversion("09:00:45PM")
timeConversion("10:00:45PM")
timeConversion("11:00:45PM")
timeConversion("12:00:45PM")
timeConversion("12:00:00AM")
timeConversion("01:00:45AM")
