import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "************@gmail.com"
host_pass = "******************"
guest_address = "*************@gmail.com"
subject = "Regarding Model Accuracy "
content = '''Hello, 
				Developer this is an email regarding to your last commit. Your last commit was taken into consideration and based on that the trained model has given best accuracy .
				Congratulations on your success.
        Accuracy of model : os.system("cat /MLops/accuracy.txt")
			THANK YOU ...'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')
