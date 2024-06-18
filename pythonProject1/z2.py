import random

# Ввод количества экзаменов и дисциплин
num_exams = int(input("Введите количество экзаменов: "))
subjects = input("Введите наименования дисциплин через запятую и пробел: ").split(', ')
subjects = [subject.strip() for subject in subjects]

# Списки дней недели, времени и номеров билетов
days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
times = [9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0]

for i in range(num_exams):
    subject = random.choice(subjects)
    exam_day = random.choice(days)
    exam_time = random.choice(times)
    ticket_number = random.randint(1, 20)

    print(
        f"Экзамен по дисциплине «{subject}» состоится в {exam_day} время {exam_time}. Ваш счастливый билет N {ticket_number}.")

    subjects.remove(subject)  # Чтобы избежать повторения дисциплин
    times.remove(exam_time)  # Исключаем время, чтобы избежать повторений
