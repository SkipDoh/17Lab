import datetime

def get_exam_date(days_to_exam):
  """Переводит количество дней до экзамена в конкретный день и месяц."""
  today = datetime.date.today()
  exam_date = today + datetime.timedelta(days=days_to_exam)
  return exam_date.strftime("%d.%m")

if __name__ == "__main__":
  days_to_exam = int(input("Введите количество дней до экзамена: "))
  exam_date = get_exam_date(days_to_exam)
  print(f"Экзамен состоится {exam_date}.")
