from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_emails, subject, body):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(recipient_emails)  # Join the list of recipients
    message['Subject'] = subject

    # Add the body text to the email
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the Gmail SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted TLS connection
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_emails, message.as_string())
        print(f"Email sent successfully to {', '.join(recipient_emails)}")

    except Exception as e:
        print(f"Failed to send email: {str(e)}")

    finally:
        server.quit()

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'hourly_dag',
    default_args=default_args,
    description='A DAG that runs every hour',
    schedule_interval='0 * * * *',  # Every hour on the hour
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    def greet():
        print()
        sender_email = 'thekiadoe@gmail.com'
        sender_password = 'kbmx nmnx ifha vnyk'  # Or app-specific password if 2FA is enabled
        recipient_emails = ['thekiadoe@gmail.com']  # List of recipients
        subject = "Hello! This DAG runs every hour on the hour."
        body = "Hello! This DAG runs every hour on the hour."
        send_email(sender_email, sender_password, recipient_emails, subject, body)
    greet_task = PythonOperator(
        task_id='greet_task',
        python_callable=greet,
    )
