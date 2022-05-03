from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.core.mail import send_mail

from .models import DetailModel, EducationModel, FacultyModel, ProfileModel
from main import forms as main_forms
from main import views as main_views



class FacultiesListView(ListView):
    context_object_name = "faculties"
    template_name = "faculty/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        context["title"] = "Институты"
        # context["admission"] = self.get_form()  
        context["details"] = DetailModel.objects.filter(page__title="Факультеты")
        
        return context  

    def get_queryset(self):
        return FacultyModel.objects.filter(status="post")


class CollagiesListView(ListView):
    context_object_name = "faculties"
    template_name="faculty/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["title"] = "Колледжи"
        context["details"] = DetailModel.objects.filter(page__title="Колледжи") 
        
        return context
    
    def get_queryset(self):
        return FacultyModel.objects.filter(status="middle")


class FacultyListView(ListView):
    context_object_name = "profiles"
    template_name="faculty/faculty.html"
    form_class = main_forms.InteresUser

    def get_faculty(self):
        return  get_object_or_404(FacultyModel, slug = self.kwargs["faculty"])

    def get_queryset(self):
        return self.get_faculty().faculty.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            object_list = self.get_faculty().faculty.all(),
            **kwargs)
        context["title"] = self.get_faculty()
        context["details"] = DetailModel.objects.filter(page__title="Колледжи") 
        
        context["programs_count"] = ProfileModel.objects.filter(faculty__slug=self.kwargs["faculty"]).count
        context["collage"] = self.get_faculty().faculty.filter(education__title="Колледж")
        context["under"] = self.get_faculty().faculty.filter(education__title="Бакалавриат")
        context["middle"] = self.get_faculty().faculty.filter(education__title="Магистратура")
        context["post"] = self.get_faculty().faculty.filter(education__title="Aспирантура")

        
        return context

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        page_name = self.get_context_data()["title"]
        main_views.get_message(self.request)
        send_mail(
            '| intuit.kg | {title}'.format(title = page_name), 
            main_views.get_message(self.request),
            main_views.EMAIL_HOST_USER, 
            [ main_views.EMAIL_HOST_USER ], 
            fail_silently=False
        )
        main_views.save_interesed_user(self.request, page_name)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super().form_invalid(form)


class EducationListView(ListView, FormView):
    context_object_name = "profiles"
    template_name="faculty/education.html"
    form_class = main_forms.InteresUser

    def get_education(self):
        return get_object_or_404(EducationModel, slug = self.kwargs["education"])

    def get_queryset(self):
        return self.get_education().education.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            object_list = self.get_education().education.all(),
            **kwargs)
        context["title"] = self.get_education()
        return context
    
    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        page_name = self.get_context_data()["title"]
        main_views.get_message(self.request)
        send_mail(
            '| intuit.kg | {title}'.format(title = page_name), 
            main_views.get_message(self.request),
            main_views.EMAIL_HOST_USER, 
            [ main_views.EMAIL_HOST_USER ], 
            fail_silently=False
        )
        main_views.save_interesed_user(self.request, page_name)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super().form_invalid(form)


class ProfileListView(TemplateView, FormView):
    template_name="faculty/profile.html"
    form_class = main_forms.InteresUser

    def get_profile(self):
        return get_object_or_404(ProfileModel, slug=self.kwargs["title"],
                                faculty__slug=self.kwargs["faculty"], 
                                education__slug=self.kwargs["education"],
                                edu_form__slug=self.kwargs["eduform"]) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = self.get_profile()
        context["title"] = context["profile"].title
        return context
    
    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        page_name = self.get_context_data()["title"]
        main_views.get_message(self.request)
        send_mail(
            '| intuit.kg | {title}'.format(title = page_name), 
            main_views.get_message(self.request),
            main_views.EMAIL_HOST_USER, 
            [ main_views.EMAIL_HOST_USER ], 
            fail_silently=False
        )
        main_views.save_interesed_user(self.request, page_name)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super().form_invalid(form)











class FacultiesFormView(FacultiesListView, FormView):
    form_class = main_forms.InteresUser

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        context["admission"] = self.get_form() 
        return context  

    def post(self, request, *args, **kwargs):
        page_name = super().get_context_data()["title"]
        form = self.get_form()
        if form.is_valid():

            main_views.get_message(request)
            send_mail(
                '| intuit.kg | {title}'.format(title = page_name), 
                main_views.get_message(request),
                main_views.EMAIL_HOST_USER, 
                [ main_views.EMAIL_HOST_USER ], 
                fail_silently=False
            )
            main_views.save_interesed_user(request, page_name)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CollagiesFormView(CollagiesListView, FormView):
    form_class = main_forms.InteresUser

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        context["admission"] = self.get_form() 
        return context  

    def post(self, request, *args, **kwargs):
        page_name = super().get_context_data()["title"]
        form = self.get_form()
        if form.is_valid():

            main_views.get_message(request)
            send_mail(
                '| intuit.kg | {title}'.format(title = page_name), 
                main_views.get_message(request),
                main_views.EMAIL_HOST_USER, 
                [ main_views.EMAIL_HOST_USER ], 
                fail_silently=False
            )
            main_views.save_interesed_user(request, page_name)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class FacultiesFormView(FacultiesListView, FormView):
    form_class = main_forms.InteresUser

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        context["admission"] = self.get_form() 
        return context  

    def post(self, request, *args, **kwargs):
        page_name = super().get_context_data()["title"]
        form = self.get_form()
        if form.is_valid():

            main_views.get_message(request)
            send_mail(
                '| intuit.kg | {title}'.format(title = page_name), 
                main_views.get_message(request),
                main_views.EMAIL_HOST_USER, 
                [ main_views.EMAIL_HOST_USER ], 
                fail_silently=False
            )
            main_views.save_interesed_user(request, page_name)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class FacultyFormView(FacultyListView, FormView):
    form_class = main_forms.InteresUser

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        context["admission"] = self.get_form() 
        return context  

    def post(self, request, *args, **kwargs):
        page_name = super().get_context_data()["title"]
        form = self.get_form()
        if form.is_valid():

            main_views.get_message(request)
            send_mail(
                '| intuit.kg | {title}'.format(title = page_name), 
                main_views.get_message(request),
                main_views.EMAIL_HOST_USER, 
                [ main_views.EMAIL_HOST_USER ], 
                fail_silently=False
            )
            main_views.save_interesed_user(request, page_name)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

