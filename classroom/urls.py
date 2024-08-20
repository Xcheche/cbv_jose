from django.urls import path
from . import views

app_name = "classroom"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("thankyou", views.ThankYouView.as_view(), name="thankyou"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("create_teacher", views.CreateTeacherView.as_view(), name="create_teacher"),
    path("teacher_list", views.TeacherListView.as_view(), name="teacher_list"),
]
