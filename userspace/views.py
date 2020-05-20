from django.shortcuts import render, reverse, HttpResponseRedirect
#from recipe_app.models import Author, Recipe
#from recipe_app.forms import recipe_form, author_form, login_form
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from userspace.models import MyUser
from userspace.forms import sign_in, create_user

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signInView(request):
    if request.method == "POST":
        form = sign_in(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                HttpResponseRedirect('profile/' + str(user.id))
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
            MyUser.objects.create(
                displayname=data['displayname'],
                username=data['username']
            )
            return HttpResponseRedirect(reverse('home'))
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
