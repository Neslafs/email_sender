from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

@login_required
def user_logout(request):
    try:
        logout(request)
        return redirect('login')
    except Exception as e:
        return HttpResponse(f"<h2>Error : {str(e)} </h2>", status=500)