#!/usr/bin/env python
# coding: utf-8

# get the full file name
import glob

# for the email
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

# keep a schedule
import time

# create kittens list from image files in your directory
kittens = glob.glob('KITTEN-IMAGE-DIRECTORY/*')

# the email function to send off the kitten gif
def send_kitten(i, kitten):
    fromaddr = "YOUR GMAIL FROM ADDRESS"
    pwd = "YOUR GMAIL PASSWORD"
    toaddr = 'THE EMAIL ADDRESS THAT RECEIVES THE KITTENS'

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "your hourly kitten gif has arrived!"
    body = "cuteness gif number {} is attached \ncheers, YOUR NAME".format(i)
    msg.attach(MIMEText(body, 'plain'))

    filename = kitten
    attachment = open(kitten, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, pwd)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    # print a confirmation in your console
    print ('kitten number {} sent '.format(i) + time.ctime())

# keep track of kitten number
i = 1

for kitten in kittens:
    print kitten
    send_kitten(i, kitten)
    i += 1
    time.sleep(3600)
