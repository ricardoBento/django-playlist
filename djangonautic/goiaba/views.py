from django.shortcuts import render

def goiaba_home(request):
    return render(request, 'goiaba_files/goiaba_home.html')
