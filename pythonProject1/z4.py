import datetime

def get_lucky_dates(start_date_str, n):
  """Получает список из трёх счастливых дат, начиная с исходной даты."""
  start_date = datetime.datetime.strptime(start_date_str, "%Y/%m/%d").date()
  lucky_dates = []
  count = 0
  current_date = start_date
  while count < 3:
    current_date += datetime.timedelta(days=n)
    day_of_week = current_date.weekday()
    day_number = current_date.day
    if day_number % 4 != 0 and day_of_week != 0:  # Не кратен 4 и не понедельник
      count += 1
      lucky_dates.append(current_date)
    else:
      continue
  return lucky_dates

def format_date(date):
  """Форматирует дату в нужный формат."""
  return date.strftime("%d %B, %A").replace(" 0", " ")

if __name__ == "__main__":
  start_date_str = input("Введите исходную дату в формате YYYY/MM/DD: ")
  n = int(input("Введите число n: "))
  lucky_dates = get_lucky_dates(start_date_str, n)
  for date in lucky_dates:
    print(format_date(date))
