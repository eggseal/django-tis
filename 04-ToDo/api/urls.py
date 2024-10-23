from django.urls import path
from .views import *

urlpatterns = [
    path('todos/', TodoListCreate.as_view(), name='list'),
    path('todos/<int:pk>', TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', TodoToggleComplete.as_view()),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]