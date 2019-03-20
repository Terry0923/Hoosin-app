from django.shortcuts import redirect

def auth_allowed(request):
    if not auth_allowed(request):
        return redirect('profiles/error.html')#<-here goes your url as defined on your urls.py
