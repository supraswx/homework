def send_email(messege, recipient, *, sender = "university.help@gmail.com"):
    for i in (recipient, sender):
        if '@' in i and '.com' in i or '@' in i and '.ru' in i or '@' in i and '.net' in i:
            result = True
            continue
        else:
            result = False
            break
    if result == False:
        print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>.")
        return
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.")



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')