import smtplib
def send(recipient ,msg):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('kursachsv@gmail.com','123321sasasa')
    smtpObj.sendmail('kursachsv@gmail.com', recipient, msg)
    smtpObj.quit()