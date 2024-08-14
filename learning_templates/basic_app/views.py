from django.shortcuts import render
from basic_app import forms

#login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    # context_dict = {'text':'hello world', 'number':100}
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("YOU ARE LOGGED IN, NICE!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    
    return render(request, 'basic_app/registration.html',{'user_form':user_form, 'registered':registered, 'profie_form':profile_form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
            
        else:
            print("SOMEONE TRIED TO LOGIN AND FAILED!")
            print("USERNAME: {} and password: {}".format(username, password))
            return HttpResponse("INVALID LOGIN DETAILS SUPPLIED!")
        
    else:
        return render( request, 'basic_app/login.html', {})












# def other(request):
#     return render(request, 'basic_app/other.html')

# def relative(request):
#     return render(request, 'basic_app/relative_url_template.html')
