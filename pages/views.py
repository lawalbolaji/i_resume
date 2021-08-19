from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

def resumeView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message successfully sent!")
            return render(request, 'resume.html', {'form': ContactForm()})
        else:
            messages.error(request, 'Invalid form submission.')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'resume.html', context)
