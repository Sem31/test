from django.contrib import admin
from django.urls import path, include

from app.views import StudentView

s1 = StudentView.as_view({
    "post": "create",
    "get": "list"
})


s2 = StudentView.as_view({
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
    # "get": "retreive",
})


urlpatterns = [
    path('student/', s1),
    path('student/<str:pk>', s2)

]