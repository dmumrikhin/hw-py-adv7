'''
Мы устроились на новую работу. Бывший сотрудник начал разрабатывать модуль для работы 
с почтой, но не успел доделать его. Код рабочий. Нужно только провести рефакторинг кода.

Создать класс для работы с почтой;
Создать методы для отправки и получения писем;
Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, 
либо аргументы методов;
Переменные должны быть названы по стандарту PEP8;
Весь остальной код должен соответствовать стандарту PEP8;
Класс должен инициализироваться в конструкции.
if __name__ == '__main__'
'''


import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser

class Post():

    def __init__(self, 
        login, 
        password, 
        gmail_smtp = "smtp.gmail.com", 
        gmail_imap = "imap.gmail.com",
        subject = 'Subject', 
        recipients = ['vasya@email.com', 'petya@email.com'],
        message = 'Message', 
        header = None
        ):

        self.gmail_smtp = gmail_smtp
        self.gmail_imap = gmail_imap
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header

    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        ms = smtplib.SMTP(self.gmail_smtp, 587) # identify ourselves to smtp gmail client
        ms.ehlo() # secure our email with tls encryption
        ms.starttls() # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())

        ms.quit()

    def receive_message(self):
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('/Users/a1/settings.ini')
    login = config['HW']['login']
    password = config['HW']['password']

    post = Post(login, password)
    post.receive_message()




