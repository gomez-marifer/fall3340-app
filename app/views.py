from django.shortcuts import render

# method
def home(request):
    return render(request, 'home.html', {})
