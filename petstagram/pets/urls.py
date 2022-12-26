from django.urls import path, include

from petstagram.pets.views import add_pet, details_pet, delete_pet, edit_pet

urlpatterns = (
    path('add/', add_pet, name='add_pet'),
    path('<str:username>/pet/<slug:peyt_name>/', include([
        path('', details_pet, name='details pet'),
        path('delete/', delete_pet, name='delete pet'),
        path('edit/', edit_pet, name='edit pet'),
    ]))

)
