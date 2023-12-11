# Time of Day Greeting: Create a program that outputs a different greeting based on the time input 
# (e.g., "Good morning!" for times in the morning).
# 6-12 good morning 
# 12-16 good afternoon
# 16-21 good evening
# 21-... good night

#OK
def dayGreeting(hour):
    if hour <= 12 and hour >= 6:
        return "good morning darling, have you slept well ?"
    elif hour <= 16:
        return "good afternoon"
    elif hour <= 21:
        return "good evening"
    else:
        return "good night and rest for next battle"
        
insertion = float(input("enter the day hour:"))
print(dayGreeting(insertion))




