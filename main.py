import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from bs4 import BeautifulSoup

# Configuration
MOVIE_NAME = "The Goat"  # Movie to check
PAYTM_TICKETS_URL = "https://paytm.com/movies/the-greatest-of-all-time-movie-detail-169146"
# PAYTM_TICKETS_URL = "https://paytm.com/movies/vaazhai-movie-detail-176695"

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "codebin.76@gmail.com"
EMAIL_PASSWORD = "kxam pptj zewp tanq"
TO_EMAIL = "arasulingam.7639@gmail.com"

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_ADDRESS, TO_EMAIL, text)
    server.quit()

def check_ticket_availability():
    try:
        # Fetch the page content
        response = requests.get(PAYTM_TICKETS_URL)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check if "Showlisting" button is present
        showlisting_button = soup.find('div', class_='Toggle_selected__ckZAN')
        
        if showlisting_button:
            print(f"Tickets for '{MOVIE_NAME}' are available!")
            subject = f"Tickets Available for {MOVIE_NAME}"
            body = f"Tickets for '{MOVIE_NAME}' are now available.\nCheck at: {PAYTM_TICKETS_URL}"
            send_email(subject, body)
            print("Mail sent")
            return True
        else:
            print(f"No tickets available for '{MOVIE_NAME}' yet.")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    i = True
    while i:
        if check_ticket_availability():
            i = False
        time.sleep(120)
