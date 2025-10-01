import smtplib
import csv
import datetime
import time
import schedule


Gmail_Address = "Sambhaji.yt@gmail.com"
Gmail_App_Password = "thaf pmoq hhuj kkmf"


def get_email_config():
    return Gmail_Address, Gmail_App_Password

def send_email(receiver, subject, message):
    try:
        print("Sending email...")
        sender, password = get_email_config()
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        
        server.login(sender, password)
        email_msg = F"Subject: {subject}\n\n{message}".encode("utf-8")
        server.sendmail(sender, receiver, email_msg)
        server.quit()
        
        print(F"Email sent successfully to : {receiver}")
    
    except smtplib.SMTPAuthenticationError as e:
        print("Authentication failed..")
        print(F"Error details: {e}")
        
    except Exception as e:
        print("Error sending email :", e)

def add_reminder(task, r_time, receiver_email, send_mode="immediate"):
    with open("Reminder.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([task, r_time, receiver_email, send_mode])
        
    print("Reminder added...")
    
    
    if send_mode == "immediate":
        subject = F"New task created :{task}"
        message = F"Task : {task}\nTime: {r_time}"
        
        send_email(receiver_email, subject, message)
        

def schedule_email(task, r_time, receiver_email):
    
    try:
        formatted_time = r_time
        subject = F"Reminder: {task}"
        message = F"Hey! Don't forget to complete: {task} at {formatted_time}"
        
        schedule.every().day.at(formatted_time).do(send_email, receiver_email, subject, message)
        print(F"Scheduled email for: {task}, at {formatted_time}")
        
    except ValueError as e:
        print(F"{e}")
        print("Please use 24-hours format like: 09:15, 14:30, or 23:45")
        
        return False
    
    except Exception as e:
        print(F"Error scheduling email: {e}")
        
        return False
        
    return True



while True:
    print("\n  Reminder System..  ")
    print("1. Add reminder")
    print("2. Add scheduled reminder")
    print("3. Run scheduled reminders")
    print("4. Exit")
    
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter task name: ")
        r_time = input("Enter task time..(HH:MM), 24 hours format")
        receiver = input("Enter receiver email: ")
        
        add_reminder(task, r_time, receiver, "immediate")
        
    
    elif choice == "2":
       task = input("Enter task name: ")
       r_time = input("Enter task time..(HH:MM), 24 hours format")
       receiver = input("Enter receiver email: ")
       
       add_reminder(task, r_time, receiver, "scheduled")
       
       if schedule_email(task, r_time, receiver):
           print("Scheduled email reminder added successfully..")
       
       else:
           print("Failed to add schedule email")
           
    elif choice == "3":
        print("Running scheduled reminders...(Keep this program open)")
        
        while True:
            schedule.run_pending()
            time.sleep(30)
            
    elif choice == "4":
        print("Exiting....")
        
        break
    
    else:
        print("Invalid choice, try again")
    