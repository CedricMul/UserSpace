from django.shortcuts import render, reverse, HttpResponseRedirect
#from recipe_app.models import Author, Recipe
#from recipe_app.forms import recipe_form, author_form, login_form
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from userspace.models import MyUser
from userspace.forms import sign_in, create_user
from django.conf import settings

# Create your views here.
def index(request):
    if settings.AUTH_USER_MODEL:
        umodel = settings.AUTH_USER_MODEL
    else:
        umodel = None
    return render(request, 'index.html', {'umodel': umodel})

def signInView(request):
    if request.method == "POST":
        form = sign_in(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            suser = authenticate(
                username=data['username'],
                password=data['password']
                )
            if suser:
                login(request, suser)
                return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('home'))
    form = sign_in()
    return render(
        request,
        'form.html',
        {'form': form}
    )

# def handle_author(request):
#     if request.method == "POST":
#         form = author_form(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Author.objects.create(
#                 name=data['name'],
#                 bio=data['bio']
#             )
#             return HttpResponseRedirect(reverse('home'))


def createUserView(request):
    if request.method == 'POST':
        form = create_user(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            x = MyUser.objects.create(
                displayname=data['displayname'],
                username=data['username'],
                password=data['password']
            )
            if x:
                login(request, x)
                return HttpResponseRedirect(reverse('home'))
        #else: 
    form = create_user()
    return render(
        request,
        'form.html',
        {'form': form}
    )

@login_required
def viewProfile(request, id):
    userProfile = MyUser.objects.get(id=id)
    return render(
        request,
        'profile.html',
        {'userProfile': userProfile}
    )

def formHandle(request, form_type):
    typeForm = {
        'createUser': createUserView(request),
        'login': signInView(request)
    }
    return typeForm[form_type]

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
