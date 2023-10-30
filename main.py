import random
import smtplib

s_email = "achiyodas@outlook.com"
s_password = "5110broadband"

r_email = input("Enter email: ")

a = random.randint(100000, 999999)
message = f"""From: Mr. x <{s_email}>
To: To Miss y <{r_email}>
Subject: Email verification

Your code: {a}
"""

try:
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login(s_email, s_password)
    server.sendmail(s_email, r_email, message)
    server.quit()

    
except Exception as exception:
    print("Error: %s!\n\n" % exception)

print("Email sent! Check your inbox or spam folder.")
i = 0
while i<3:
    code = int(input("enter the code: "))
    if code==a:
        print("Email verified succussfully!")
        break
    else:
        print("invalid input! "+ "you have "+str((3-i))+" chance to write the correct code.")
        i+=1
