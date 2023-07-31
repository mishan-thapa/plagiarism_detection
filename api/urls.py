from django.urls import path
from . import views
from .views import create_book, pos_tagging

urlpatterns =[
    path('', views.getData, name="getwala"),
    path('synset/', create_book.as_view(), name='synset'),
    path('pos_tagging/', pos_tagging.as_view(), name='pos_tagging'),
]


#    path('create/', views.create_book, name='create-book'),
#
#