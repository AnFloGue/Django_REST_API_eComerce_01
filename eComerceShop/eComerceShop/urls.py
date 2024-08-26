from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# Define a simple view for the root URL
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product.urls')),
    path('', home),  # Add this line to handle the root URL
]