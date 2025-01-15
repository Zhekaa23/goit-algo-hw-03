import datetime


def get_days_from_today(date: str) -> int:
    try:
        input_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return "Неправильний формат дати , заупстіть програму ще раз)"
    current_date = datetime.date.today()
    result = current_date - input_date
    return result.days


our_date = input("Enter your date in format Year/month/day like 2000-11-21 - ")
print(get_days_from_today(our_date))
