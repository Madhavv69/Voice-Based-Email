Voice-Based Email System for Visually Impaired
This project is designed to assist visually impaired individuals in composing and managing emails using voice commands. The system integrates speech recognition and synthesis technologies to facilitate hands-free email interaction.

Features
Compose Emails: Users can compose emails by dictating the recipient's email address, subject, and content.
Check Inbox: Users can listen to their inbox emails, with options to read the sender, subject, and body of each email.
Logout: Allows users to safely log out of their email account.
Technologies Used
Python: Backend logic for email composition, inbox retrieval, and interaction.
SpeechRecognition: Library for converting speech to text.
gTTS (Google Text-to-Speech): Converts text into spoken words for user interaction.
smtplib, imaplib: Libraries for sending and receiving emails using SMTP and IMAP protocols.
Beautiful Soup: Used for parsing email content from HTML emails.
Setup Instructions
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/Voice-Based-Email-System.git
cd Voice-Based-Email-System
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Set Environment Variables

Create a .env file in the project directory.
Add your email credentials:
makefile
Copy code
EMAIL_USER=your_email@gmail.com
EMAIL_APP_PASS=your_app_password
Run the Application

bash
Copy code
python main.py
Interact with the Application

Follow the voice prompts to compose emails, check inbox, or logout.
Speak clearly and wait for the system to process your commands.
Project Structure
main.py: Main script for running the voice-based email system.
utils.py: Utility functions including email preprocessing and speech functions.
README.md: Documentation file providing information about the project.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

