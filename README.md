# Voice-Based Email System for Visually Impaired
This project is designed to assist visually impaired individuals in composing and managing emails using voice commands. The system integrates speech recognition and synthesis technologies to facilitate hands-free email interaction.

## FeaturesCompose 
* Emails: Users can compose emails by dictating the recipient's email address, subject, and content.
* Check Inbox: Users can listen to their inbox emails, with options to read the sender, subject, and body of each email.
* Logout: Allows users to safely log out of their email account.

## Technologies Used
* Python: Backend logic for email composition, inbox retrieval, and interaction.
* SpeechRecognition: Library for converting speech to text.
* gTTS (Google Text-to-Speech): Converts text into spoken words for user interaction.
* smtplib, imaplib: Libraries for sending and receiving emails using SMTP and IMAP protocols.
* Beautiful Soup: Used for parsing email content from HTML emails.

## Setup Instructions
1. **Clone the Repository:**
    ```bash
    git clone https:https://github.com/Madhavv69/Hand-Gesture-Recognition-and-Voice-Conversion-for-Deaf-and-Dumb.git
    cd Voice-Based-Email-System
    ```

2. **Install Dependencies:**
    ```bash
   pip install -r requirements.txt
    ```

3. **Set Environment Variables:**
   * Create a .env file in the project directory.
  * Add your email credentials:
    ```bash
    EMAIL_USER=your_email@gmail.com
    EMAIL_APP_PASS=your_app_password

    ```

