from django.contrib import admin
from django.urls import path, include

# urls possíveis 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),

]




