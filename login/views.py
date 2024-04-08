from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View

def index(request):
    return render(request ,"index.html")

@login_required
def home(request):
    return render(request, 'home.html')
# Create your views here.

# class CustomErrorView(View):
#     def get(self, request):
#         return render(request, 'error.html')


def hello_world(request):
    return Exception("This is the test error")
   
def custom_404(request, exception):
    return render(request, 'error_404.html', status=404)

def custom_500(request):
    return render(request ,'error_500.html', status=500)
