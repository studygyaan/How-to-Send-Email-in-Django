from django.shortcuts import render

from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail

class SendFormEmail(View):

    def  get(self, request):

        # Get the form data 
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        send_mail(
            'Subject - Django Email Testing', 
            'Hello ' + name + ',\n' + message, 
            'sender@example.com', # Admin
            [
                email,
            ]
        )

        send_mail(
            'subject', 
            'body of the message', 
            'sender@example.com', 
            [
                'receiver1@example.com', 
                'receiver2@example.com'
            ]
        )

        message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
        message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
        send_mass_mail((message1, message2), fail_silently=False)

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return redirect('home')


