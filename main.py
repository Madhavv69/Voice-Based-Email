import os
import imaplib
import smtplib
import speech_recognition as sr
from bs4 import BeautifulSoup
import email
from gtts import gTTS
import pyglet
import time
import re

# Function to preprocess spoken email address
def preprocess_email_address(text):
    # Convert number words to digits
    number_words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    for word, digit in number_words.items():
        text = text.replace(word, digit)

    # Remove spaces and convert to lowercase
    text = text.replace(' ', '').lower()

    # Remove any remaining white spaces
    text = ''.join(text.split())

    # Replace spoken symbols with actual symbols
    text = text.replace('attherate', '@').replace('at', '@')
    text = text.replace('dot', '.')

    return text

# Function to handle voice input and convert to text
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording done.")
        audio = r.listen(source)
        print("Recording complete.")

    try:
        text = r.recognize_google(audio).lower()
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Function to handle voice output using gTTS and pyglet
def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tsname = "C:\\Users\\Chinu\\Desktop\\Python\\Project\\path\\name.mp3"
    tts.save(tsname)

    music = pyglet.media.load(tsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(tsname)

# Main part of the script
while True:
    print("-" * 60)
    print("       Project: Voice based Email for visually impaired")
    print("-" * 60)

    # Speak project announcement
    speak_text("Project: Voice based Email for visually impaired")

    # Login from OS
    login = os.getlogin()
    print("You are logged in from: " + login)

    # Choices
    speak_text("Option 1. Compose a mail.")
    print("1. Compose a mail.")

    speak_text("Option 2. Check your inbox")
    print("2. Check your inbox")

    speak_text("Option 3. Logout")
    print("3. Logout")

    # Get user choice
    speak_text("Your choice")
    print("Your choice:")

    text = recognize_speech()

    # Process choice
    if text.startswith("option one") or text.startswith("option 1"):
        text = "1"
    elif text.startswith("option two") or text.startswith("option 2"):
        text = "2"
    elif text.startswith("option three") or text.startswith("option 3") or text.startswith("option free"):
        text = "3"

    if text.isdigit():
        if int(text) == 1:
            # Compose a mail logic
            speak_text("Please say the recipient's email address.")
            print("Please say the recipient's email address:")
            recipient_email = recognize_speech()

            # Preprocess the email address
            recipient_email = preprocess_email_address(recipient_email)

            speak_text("Please say the subject of your email.")
            print("Please say the subject of your email:")
            email_subject = recognize_speech()

            speak_text("Please start dictating your email content. Say 'done' when finished.")
            print("Please start dictating your email content. Say 'done' when finished.")

            # Record email content until user says 'done'
            email_content = ""
            while True:
                text1 = recognize_speech()
                if text1 == "done":
                    break
                email_content += text1 + " "

            email_user = os.getenv('EMAIL_USER')
            email_app_pass = os.getenv('EMAIL_APP_PASS')

            mail = smtplib.SMTP('smtp.gmail.com', 587)  # Host and port area
            mail.ehlo()  # Hostname to send for this command defaults to the FQDN of the local host.
            mail.starttls()  # Security connection
            mail.login(email_user, email_app_pass)  # Login section
            mail.sendmail(email_user, recipient_email, f"Subject: {email_subject}\n\n{email_content}")  # Send section
            print(f"Congrats! Your mail has been sent to {recipient_email}.")
            speak_text(f"Congrats! Your mail has been sent to {recipient_email}.")
            mail.close()

        elif int(text) == 2:
            # Check inbox logic
            email_user = os.getenv('EMAIL_USER')
            email_pass = os.getenv('EMAIL_APP_PASS')

            try:
                mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)  # Host and port area with SSL security
                mail.login(email_user, email_pass)  # Login
                mail.select('Inbox')  # Select inbox

                # Fetch email details
                status, total = mail.select('Inbox')
                print("Number of mails in your inbox: " + str(total[0].decode('utf-8')))
                speak_text("Total mails are: " + str(total[0].decode('utf-8')))

                result, unseen = mail.search(None, 'UnSeen')
                unseen_count = len(unseen[0].split())
                print("Number of UnSeen mails: " + str(unseen_count))
                speak_text("Your Unseen mails: " + str(unseen_count))

                inbox_item_list = mail.uid('search', None, "ALL")[1][0].split()
                print("Reading the most recent emails:")
                speak_text("Reading the most recent emails:")

                for email_uid in reversed(inbox_item_list):
                    result, email_data = mail.uid('fetch', email_uid, '(RFC822)')
                    raw_email = email_data[0][1].decode("utf-8")
                    msg = email.message_from_string(raw_email)

                    # Extracting email details
                    from_header = email.utils.parseaddr(msg['From'])[1]
                    subject_header = msg['Subject']

                    # Print and speak email details
                    print(f"From: {from_header}")
                    print(f"Subject: {subject_header}")
                    speak_text(f"From: {from_header} And Subject: {subject_header}")

                    # Get email body
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            if "attachment" not in content_disposition:
                                payload = part.get_payload(decode=True)
                                if payload:
                                    body = payload.decode()
                                    body = BeautifulSoup(body, 'html.parser').get_text()
                                    body = re.sub(r'\s+', ' ', body).strip()
                                    print("Body: " + body)
                                    speak_text("Body: " + body)
                    else:
                        body = msg.get_payload(decode=True)
                        if body:
                            body = body.decode()
                            body = BeautifulSoup(body, 'html.parser').get_text()
                            body = re.sub(r'\s+', ' ', body).strip()
                            print("Body: " + body)
                            speak_text("Body: " + body)

                    speak_text("Say 'Next' for reading another email or 'Stop' to end.")
                    print("Say 'Next' for reading another email or 'Stop' to end:")
                    choice = recognize_speech().lower()

                    while True:
                        if choice.startswith('next'):
                            break
                        elif choice.startswith('stop'):
                            break
                        else:
                            speak_text("Invalid command. Please say 'Next' or 'Stop'.")
                            print("Invalid command. Please say 'Next' or 'Stop'.")
                            choice = recognize_speech().lower()

                    if choice.startswith('stop'):
                        break

                mail.close()
                mail.logout()

            except imaplib.IMAP4.error as e:
                print(f"IMAP login failed: {e}")
                speak_text("There was an issue logging in to your email. Please try again later.")

        elif int(text) == 3:
            # Logout logic
            print("Logging out...")
            speak_text("Logging out.")
            break  # Exit the loop to logout

    else:
        print("Invalid choice. Please speak 'option one', 'option two', or 'option three'.")
        speak_text("Invalid choice. Please speak 'option one', 'option two', or 'option three'.")

print("Thank you for using Voice based Email for visually impaired.")
speak_text("Thank you for using Voice based Email for visually impaired.")
