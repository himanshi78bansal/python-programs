import tkinter as tk
import smtplib

def send_email():
    # Get the values entered in the GUI
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)
    
    # Create the email message
    message = f"Subject: {subject}\n\n{body}"
    
    # Connect to the SMTP server and send the message
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("your-email@gmail.com", "your-email-password")
        smtp.sendmail("your-email@gmail.com", recipient, message)
    
    # Display a confirmation message
    confirmation_label.config(text="Email sent!")

# Create the main window
root = tk.Tk()
root.title("Send Email")

# Create the GUI widgets
recipient_label = tk.Label(root, text="Recipient:")
recipient_entry = tk.Entry(root)
subject_label = tk.Label(root, text="Subject:")
subject_entry = tk.Entry(root)
body_label = tk.Label(root, text="Body:")
body_text = tk.Text(root)
send_button = tk.Button(root, text="Send", command=send_email)
confirmation_label = tk.Label(root, text="")

# Add the widgets to the window
recipient_label.pack()
recipient_entry.pack()
subject_label.pack()
subject_entry.pack()
body_label.pack()
body_text.pack()
send_button.pack()
confirmation_label.pack()

# Start the main event loop
root.mainloop()
