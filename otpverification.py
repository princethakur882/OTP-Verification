# First I will generate a random number and store it in a variable which I will be using while sending emails to the users:
import os
import math
import random
import smtplib


digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
#you need to have your Google app password to be able to send emails using your Gmail account. For this task, you need to follow the steps mentioned bellow :
# 1. Go to your Google Account.
# 2. Select Security.
# 3. Under “Signing in to Google,” select App Passwords.
# 4. If you don’t have App Password option, it might be because:
# ● 2-Step Verification is not set up for your account.
# ● 2-Step Verification is only set up for security keys.
# ● Your account is through work, school, or other organization.
# ● You turned on Advanced Protection.
# 5. At the bottom, choose >Select app and choose the app you using and then >Select device and choose the device you’re using and then Generate.
# 6. Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
# 7. Tap Done.
s.login("Your Gmail Account", "You app password")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")