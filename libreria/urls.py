"""libreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from core.views import bookListView, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    #url para panel admin
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('book_list/', bookListView.as_view(), name='book_list'),
    path('book_register/', BookCreate.as_view(), name='book_register'),
    path('book_deleted/<str:pk>/', BookDelete.as_view(), name='book_deleted'),
    path('book_edit/<str:pk>/', BookUpdate.as_view(), name='book_edit'),
]


