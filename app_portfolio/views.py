from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from django.core.mail import send_mail
from .forms import ContactForm

from .models import Project
class Home(View):
    def get(self,request):
        
        return render(request,'index.html')
    
class About(View):
    def get(self,request):
        
        return render(request,'about.html')

    
class Projects(View):
    def get(self,request):
        gallery_items = Project.objects.all()
        return render(request,'projects.html',{'gallery_items':gallery_items})

class Resume(View):
    def get(self,request):
        form = ContactForm()
        return render(request,'resume.html',{'form':form})
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = f"Nombre: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMensaje:\n{form.cleaned_data['message']}"
            send_mail(subject, message, 'luisernestoperezbello@gmail.com', ['luisernestoperezbello@gmail.com'])
            print(f'{message}')
            return redirect('/')  
        else:
            return render(request,'resume.html',{'form':form})