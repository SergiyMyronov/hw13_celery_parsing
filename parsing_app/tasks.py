from celery import shared_task

from django.core.mail import send_mail as django_send_mail

from parsing_app.parsing import parsing_html as main_parsing_html


@shared_task
def send_mail(subject, message, from_email, recipient_list):
    django_send_mail(subject, message, from_email, recipient_list)


@shared_task
def parsing_html():
    quotes = main_parsing_html()
    if quotes:
        subject = 'Authors and their quotes'
        from_email = 'noreply@test.com'
        recipient_list = ['sergemk@entecheco.com']
        message = 'All quotes are added!'
        send_mail.delay(subject, message, from_email, recipient_list)
    return quotes
