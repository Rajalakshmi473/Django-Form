from django.shortcuts import render
from .forms import ContactForm

def sign_up(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'Forms/signup.html', {'form': form})
