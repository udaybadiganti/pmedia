from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserRegisterForm, UserLogInForm
from django.contrib.auth.decorators import login_required

# Create your views here.
########################### login and signin module ################################################
def login_view(request):
    next = request.GET.get('next')
    form = UserLogInForm(request.POST, None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username = username, password = password)

        login(request, user)
        if next:
            return redirect(next)
        return redirect('/andhrapradesh/')

    context = {
            'form' : form,
    }

    return render(request, 'login.html', context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST, None)

    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password = password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/andhrapradesh/')

    context = {
            'form' : form,
    }

    return render(request, 'signin.html', context)

'''
def logout_view(request):
    """
    Removes the authenticated user's ID from the request and flushes their
    session data.
    """
    # Dispatch the signal before the user is logged out so the receivers have a
    # chance to find out *who* logged out.
    user = getattr(request, 'user', None)
    if hasattr(user, 'is_authenticated') and not user.is_authenticated():
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)

    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()
    return redirect('/')
'''

def logout_view(request):
#    for sesskey in request.session.keys():
#        del request.session[sesskey]
    auth.logout(request)
    return redirect('/')

########################### end of login and signin module ################################################
