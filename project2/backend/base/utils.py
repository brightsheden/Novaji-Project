from django.core.mail import send_mail
from django.utils.html import strip_tags


def sendAccountCreationEmail(user):
    # HTML email template
    email = user['email']
    username = user['username']
    token = user['token']

    html_message = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Account Created - Novaji IntroServe</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
                border-radius: 5px;
            }}
            .header {{
                background-color: #3498db;
                color: white;
                text-align: center;
                padding: 10px;
                border-radius: 5px 5px 0 0;
            }}
            .content {{
                background-color: white;
                padding: 20px;
                border-radius: 0 0 5px 5px;
            }}
            .passcode {{
                font-size: 18px;
                font-weight: bold;
                text-align: center;
                color: #3498db;
                margin: 20px 0;
            }}
            a {{
                color: #3498db;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Account Created - Novaji IntroServe</h1>
            </div>
            <div class="content">
                <p>Congratulations, your Novaji IntroServe account has been created successfully!</p>
                <p>Hello {username},</p>
                <p>Your account details:</p>
                <ul>
                    <li>Email: {email}</li>
                    <li>Username: {username}</li>
                </ul>
                <p>To complete your registration, please follow these steps:</p>
                <ol>
                    <li>Click the link below and verify your email</li>
                </ol>
                <a href="http://localhost:5173/verifyemail?token={token}">Set Password</a>
                <p>If you didn't request this email, please ignore it or contact our support team if you have any concerns.</p>
                <p>Best regards,<br>The Novaji IntroServe Team</p>
            </div>
        </div>
    </body>
    </html>
    """

    email_subject = 'Account Created - Novaji IntroServe'
    text_message = strip_tags(html_message)  
    from_email = 'shedenbright@gmail.com' 
    recipient_list = [email]
    
    send_mail(
        email_subject,
        text_message,
        from_email,
        recipient_list,
        html_message=html_message,
        fail_silently=False
    )