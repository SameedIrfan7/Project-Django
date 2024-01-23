from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Query


def contact(request):
    if request.method == 'POST':
        # Extracting data from the form
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Saving data to the database
        query = Query(name=name, email=email, subject=subject, message=message)
        query.save()

        # Sending email notification
        send_mail(
            'New User Query',
            f'Hello!\n\n{name} ({email}) has contacted you with the following details:\n\nSubject: {subject}\nMessage: {message}',
            settings.EMAIL_HOST_USER,
            ['sameedirfan7@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'thank_you.html')  # You can create a thank_you.html template for a confirmation message
    else:
        return render(request, 'contact.html')  # You can create a contact.html template for the contact form



# Create your views here.
def home(req):
    return render(req, "index.html")


def about(req):
    return render(req, "about.html")


def services(req):
    return render(req, "services.html")


def resume(req):
    return render(req, "resume.html")


def portfolio1(req):
    return render(req, "portfolio.html")


def portfolio2(req):
    return render(req, "portfolio-details.html")

