# Django imports
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import get_template

# Project imports
from .forms import ContactForm


def index(request):
    return render(request, 'frontend/index.html')

def contact(request):
    form = ContactForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            template = get_template('email_template.txt')
            context['name'] = form.cleaned_data.get('name')
            context['email'] = form.cleaned_data.get('email')
            context['message'] = form.cleaned_data.get('message')
            content = template.render(context)
            send_mail(
                'Message From mattmyoung.com',
                content,
                'admin@forwardvibe.com',
                ['matt@forwardvibe.com'],
                fail_silently=False,
            )
            context['success'] = 'Your message has been sent!'

    return render(request, 'frontend/contact.html', context)
