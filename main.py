import random
import smtplib
from tkinter import *

root = Tk()
root.geometry("500x270")
root.title("OTP Verification")

s_email = "youremail@outlook.com" #i use outlook because gmail Less secure app access is not working
s_password = "youremailpassword"
attempts = 0  # To track the number of attempts

# Function to send OTP
def send_otp():
    global attempts
    r_email_text = r_email.get()
    a = random.randint(100000, 999999) #generating code
    message = f"Subject: Email verification\n\nYour code: {a}"
    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(s_email, s_password)
        server.sendmail(s_email, r_email_text, message)
        server.quit()
        success = Label(root, text="Email sent! Check your inbox or spam folder", fg="green")
        success.grid(row=3, column=0, columnspan=2, pady=10)
        verify_otp(a)  # Call verification function after sending the email
    except Exception as exception:
        er = Label(root, text="Error: %s!\n\n" % exception, fg="red")
        er.grid(row=3, column=0, columnspan=2, pady=10)

# Function to verify OTP
def verify_otp(a):
    def check_code():
        global attempts
        entered_code = code.get()
        if entered_code == str(a):
            verified = Label(root, text="Email verified successfully!", fg="green")
            verified.grid(row=5, column=0, columnspan=2, pady=10)
        else:
            attempts += 1
            remaining_chances = 3 - attempts
            if remaining_chances > 0:
                invalid = Label(root, text=f"Invalid input! You have {remaining_chances} chance(s) to write the correct code.", fg="red")
                invalid.grid(row=4, column=0, columnspan=2, pady=10)
            else:
                no_attempts_left = Label(root, text="No more attempts left. Please try again.", fg="red")
                no_attempts_left.grid(row=4, column=0, columnspan=2, pady=10)

    code = Entry(root, show="*", width=20, font=('Arial', 12))
    code.grid(row=2, column=0, columnspan=2, pady=10)
    code.insert(0, "Enter Code")

    verify_button = Button(root, text="Verify", command=check_code, bg="blue", fg="white")
    verify_button.grid(row=2, column=2, padx=5)

# Header Label
header = Label(root, text="OTP Verification", font=("Arial", 18, "bold"))
header.grid(row=0, column=0, columnspan=3, pady=10)

# Email Entry
r_email = Entry(root, width=30, font=('Arial', 12))
r_email.grid(row=1, column=0, columnspan=3, pady=10)
r_email.insert(0, "Enter Your Email")

# Send OTP Button
send_button = Button(root, text="Send OTP", command=send_otp, bg="green", fg="white")
send_button.grid(row=1, column=3, padx=5)

root.mainloop()
