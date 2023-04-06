from django.shortcuts import render


def user_register(request):
    return render(request, "app_user/register.html", {})


def user_login(request):
    pass


def user_logout(request):
    pass
