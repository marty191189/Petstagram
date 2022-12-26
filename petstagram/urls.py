"""petstagram URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.common.urls')),
    path('accounts/', include('petstagram.accounts.urls')),
    path('pets/', include('petstagram.pets.urls')),
    path('photos/', include('petstagram.photos.urls')),
]

'''

After 'startapp APP_NAME'

1. Create 'APP_NAME/urls.py' with empty 'urlpatters'
2. Include 'APP_NAME/urls.py' into project's urls.py
3. Add 'APP_NAME' to 'INSTALLED_APPS' in settings.py
4. Open every app's dir -> apps.py and change 'name' = APP_NAME to 'name' = PROJECT.APP_NAME

'''
