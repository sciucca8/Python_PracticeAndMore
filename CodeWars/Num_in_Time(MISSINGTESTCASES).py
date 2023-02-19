def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    strtime = ""
    minutes = int(seconds / 60) # num minuts
    hours = int(minutes / 60) # num hours
    days = int(hours / 24) # num days
    years = int(days / 365) # num years
    
    sec = ("and " if seconds % 60 > 0 and seconds > 60 else "") + str(seconds % 60) + (" seconds" if seconds % 60 != 1 else " second")
    
    min = ("and " if seconds % 60 == 0 and minutes / 60 > 60 else "") + str(minutes  % 60) + (" minutes" if minutes % 60 != 1 else " minute") + (" " if sec.split()[0] == "and" else "")
    
    hour = str(hours % 24) + (" hours" if hours % 24 != 1 else " hour") + ("" if (hours % 24 == 0) else (", " if (minutes % 60 != 0 and seconds % 60 != 0) else " " ))   
    
    day = str(days % 365) + (" days" if days % 365 != 1 else " day") + ("" if not(sec and min and hour) else (" " if (sec or min or hour) and (sec and min) == 0 or (sec and hour) == 0 or (min and hour) == 0 else ", "))    
    
    year = str(years) + (" years" if years != 1 else " year") + (", " if days % 365 != 0 else " ")
     
    times = [year, day, hour, min, sec]
    print(hour)
    
    for t in times:
        print(t)
        if t[0] == "0" or t[4] == "0":
            continue
        else:
            strtime = strtime + t 
            print(strtime)

    return strtime.strip()

result = format_duration(1892250000)
print(result)
