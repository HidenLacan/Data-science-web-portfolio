from django.shortcuts import render
from django.views import View
# Create your views here.

class Home(View):
    def get(self,request):
        
        return render(request,'index.html')
    
class About(View):
    def get(self,request):
        
        return render(request,'about.html')

    
class Projects(View):
    def get(self,request):
        
        return render(request,'projects.html')

class Resume(View):
    def get(self,request):
        
        return render(request,'resume.html')