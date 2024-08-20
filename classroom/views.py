from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView
from django.contrib import messages
from classroom.forms import ContactForm
from classroom.models import Contact, Teacher

# Create your views here.


class HomeView(TemplateView):
    template_name = "classroom/home.html" # Template  view


class ThankYouView(TemplateView):
    template_name = "classroom/thankyou.html" # Template  view

# Form View
class ContactView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"
    success_url = reverse_lazy("classroom:home")

    def form_valid(self, form):
        # Access cleaned data
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]

        messages.success(self.request, f"Thanks {name} for your message!")
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        print(name, email, message)

        return super().form_valid(form)
# Create View
class CreateTeacherView(CreateView):
    model = Teacher
    fields = ["first_name", "last_name", "subject"]
    template_name = "classroom/create_teacher.html"
    
    success_url = reverse_lazy("classroom:home")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f" {form.cleaned_data['first_name']} {form.cleaned_data['last_name']} has been created")
        return response
    
# List View

class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by("-first_name")
   #template_name = "classroom/teacher_list.html"
    context_object_name = "teachers"
    