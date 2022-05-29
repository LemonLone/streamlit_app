import smtplib
EMAIL_ADDRESS = "2452893543@qq.com"
EMAIL_PASSWORD = "bsppubdbweyedieh"
smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

sender = EMAIL_ADDRESS
receiver = EMAIL_ADDRESS

subject = "Python email subject"
body = "Hello, this is an email sent by python"
msg = f"subject:{subject}\n\n{body}"

smtp.sendmail(sender,receiver,msg)
print("over!")