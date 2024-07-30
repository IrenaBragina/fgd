def chek_email(email):
    if (
        "@" in email and
        email.endswith((".com", ".ru", ".net"))):
        res = True
    else:
        res = False

def send_email(message, recipient, sender = "university.help@gmail.com"):
    if not (chek_email(sender) and chek_email(recipient)):
        result = f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    elif sender == recipient:
        result ="Нельзя отправить письмо самому себе!"
    elif sender == "university.help@gmail.com":
        result = f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}"
    else:
        result = f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}"
    print(result)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')