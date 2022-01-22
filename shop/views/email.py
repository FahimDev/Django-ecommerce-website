from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


SMTP_EMAIL = 'no-reply@tnd.com'

def send_email(subject, body_temp, send_to):
    #email_temp = render_to_string('email/review_approve.html', {'name': 'TestName'})

    send_mail = EmailMultiAlternatives(
    subject,
    body_temp,
    SMTP_EMAIL,
    [send_to],
    )

    #html_content = '<p>This is an <strong>important</strong> message.</p>'
    #end_mail.attach_alternative(html_content, "text/html")
    send_mail.fail_silently=False
    send_mail.send()