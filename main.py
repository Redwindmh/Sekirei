import smtplib
from config import GMAIL_ADDY, GMAIL_PASS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

my_addy = GMAIL_ADDY
addy_pass = GMAIL_PASS
recipient = "malhendricks@gmail.com"

gmail_server = "smtp.gmail.com"
gmail_port = 587

mail_server = smtplib.SMTP(gmail_server, gmail_port)
mail_server.ehlo()
mail_server.starttls()

message = MIMEMultipart("alternative")

mail_text = "This is a test. Nothing more, nothing lest."
message.attach(MIMEText(mail_text))

# # For attaching images
# image_path = "./attachments/"
# image_file = open(image_path, 'rb').read()
# message.attach(MIMEImage(image_file, name=os.path.basename(image_path)))
#
# # For attaching non-image files
# attachment_path = "./attachments/"
# with open(attachment_path, 'rb') as atch:
#     file = MIMEApplication(
#         atch.read(),
#         name=os.path.basename(attachment_path)
#     )
#     file['Content-Disposition'] = f'attachment;
#     filename="{os.path.basename(attachment_path)}"'
#     message.attach(file)

mail_server.login(my_addy, addy_pass)

mail_server.sendmail(
    from_addr=my_addy,
    to_addrs=recipient,
    msg=mail_text,
)

mail_server.close()
