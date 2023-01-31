
from django.urls import path
from rpgsheet.views import list_view, detail_view, post_view

urlpatterns = [
    path('', list_view),
    path('post/', post_view),
    path('<str:key>/', detail_view),
]
