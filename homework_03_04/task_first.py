from datetime import datetime

def get_days_from_today(date):
    today = datetime.today().date()

    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    
    delta = given_date - today
    
    return delta.days

print(get_days_from_today("2024-06-08")) 

