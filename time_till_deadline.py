from datetime import datetime

def convert_duration(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f"{int(days)} days, {int(hours)} hrs, {int(minutes)} min, {int(seconds)} sec"

user_input = input("Enter your goal with a dealine separated by colon(Please use DD.MM.YYYY format.) : \n").split(":")

try:
    if len(user_input) < 2:
        print(f"Please provide both goals and deadline\n")
    else:
        goal = user_input[0]
        deadline =user_input[1].strip()

        # # Attempt to convert the string to a date(parse) using the given format  
        deadline_date = datetime.strptime(deadline,"%d.%m.%Y")
        current_date = datetime.today()

        # Calculate the time remaining
        left_days=deadline_date - current_date
        #left_hours = int(left_days.total_seconds()/60/60)
        converted_hours =convert_duration(left_days.total_seconds())
        print(f"Dear user, time remaining for your goal : {goal} is {converted_hours}")
        #print(f"Dear user, time remaining for your goal : {goal} is {left_hours} hours")
    
except ValueError:
    print(f"Invalid date format for deadline {deadline}. Please use DD.MM.YYYY format.")

except IndexError as e:
    print(f"Error: {str(e)}")

except Exception as e:
    print(f"An unexpected error occured: {str(e)}")

    
    