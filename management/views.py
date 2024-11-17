from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from management.models import contact

def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('comment')
        
        contactData = contact(name=name, email=email, subject=subject, message=message)
        contactData.save()
        
        # Add a success message
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('index')  # Redirect to the index page or wherever you want
    else:
        return render(request, 'index.html')
