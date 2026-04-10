from django.shortcuts import render
from .models import MenuItem
from .forms import ContactForm

def home(request):
    return render(request, 'cafe/home.html')

def about(request):
    return render(request, 'cafe/about.html')

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'cafe/menu.html', {'items': items})

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # later save in database or send email
    return render(request, 'cafe/contact.html', {'form': form})