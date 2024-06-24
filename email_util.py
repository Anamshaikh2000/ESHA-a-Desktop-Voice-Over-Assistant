import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"
    smtp_server = "smtp.example.com"
    smtp_port = 587  # Example SMTP port, change it according to your email provider

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach body to the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        # Login to the email account
        server.login(sender_email, sender_password)
        # Send email
        server.sendmail(sender_email, to_email, msg.as_string())
        # Close the connection
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    # Example usage
    subject = "Test Email"
    body = "This is a test email from Esha assistant."
    to_email = "recipient@example.com"
    send_email(subject, body, to_email)
