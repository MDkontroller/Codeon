import os
from dotenv import load_dotenv
from email_service import AWSSESService
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()


def send_test_email():
    # Create email service instance
    email_service = AWSSESService({
        'AWS_ACCESS_KEY': os.getenv('AWS_ACCESS_KEY_ID'),
        'AWS_SECRET_KEY': os.getenv('AWS_SECRET_ACCESS_KEY'),
        'AWS_REGION': os.getenv('AWS_REGION', 'us-west-2'),
        'DEFAULT_SENDER': os.getenv('DEFAULT_SENDER')
    })

    # Verify configuration
    if not email_service.is_configured():
        print("Email service is not properly configured!")
        return False

    # Use a verified recipient email address
    recipient = "lovieokum@gmail.com"  # CHANGE THIS

    print(f"Sending test email to {recipient}...")

    # Send email
    result = email_service.send_email(
        subject="Test Email for Our Copilot",
        recipients=[recipient],
        text_body="This is your certificate, thanks for participating.",
        html_body="<h1>Test Email</h1><p>This is your certificate<b>and a test email</b> thanks for participating.</p>"
    )

    if result:
        print("Email request accepted! Check your inbox in a few minutes.")
        return True
    else:
        print("Failed to send email. Check logs for details.")
        return False


if __name__ == "__main__":
    send_test_email()
