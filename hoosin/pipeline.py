from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required



# if "@virginia.edu" in email:
#     messages.success(request, f'Your account has been created! You are now able to log in')
#     return redirect('login')
# else:
#     return redirect(request, 'profiles/error.html')

    # if not request.auth_allowed(request):
    #     return render(request, 'error')#<-here goes your url as defined on your urls.py
