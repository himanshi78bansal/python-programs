import smtplib

# Set up the connection to the SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()  # Identify yourself to the SMTP server
    smtp.starttls()  # Enable encryption for the connection
    smtp.ehlo()  # Re-identify yourself to the SMTP server after encryption
    smtp.login('your-email@gmail.com', 'your-email-password')  # Log in to the SMTP server

    # Create the email message
    subject = 'Test Email'
    body = 'This is a test email.'
    message = f'Subject: {subject}\n\n{body}'
    sender = 'your-email@gmail.com'
    recipient = 'recipient-email@example.com'

    # Send the email message
    smtp.sendmail(sender, recipient, message)

    # Log out of the SMTP server
    smtp.quit()
