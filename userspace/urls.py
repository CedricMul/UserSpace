from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from userspace import views

urlpatterns = [
    path('', views.index, name='home'),
    path('createUser/', views.createUserView),
    path('login/', views.signInView),
    path('profile/<int:id>', views.viewProfile),
    path('<str:form_type>/form/', views.formHandle)
]