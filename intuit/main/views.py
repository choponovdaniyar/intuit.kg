from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.core.mail import send_mail


from . import utils
from . import forms
from . import models
from faculty.models import DetailModel, SpecialAbilitiesModel, ProfileModel, TeacherModel, PagesModel
from news.models import PostModel
from intuit.settings import EMAIL_HOST_USER



def get_message(request):
    message = 'Данные формы:\n\n'
    for x in request.POST:
        key = x
        if key == 'csrfmiddlewaretoken' or "quiz" in key:
            continue
        value = request.POST.get(key)
        message += "{k}: {v}\n".format(k=key, v=value)
    return message

def save_interesed_user(request, page_name):
    if page_name == "Абитуриентам":
        category = models.InteresCategoryModel.objects.get(title="Консультатция приемной комиссии")
    else:
        models.InteresCategoryModel.objects.get_or_create(title=page_name)
        category = models.InteresCategoryModel.objects.get(title=page_name)
    
    user = models.InteresUserModel()
    
    # сохранение
    user.user = request.POST.get("user")
    user.phone = request.POST.get("phone")
    user.category = category 
    
    user.save()


class MainView(utils.FormsView):
    '''
        Главная страница
    '''
    template_name = "main/index.html"
    extra_context = {"page": "Главная",  "quiz": forms.ChoiceProgram(),
            "go_to": forms.InteresUser()}
    forms = [forms.ChoiceProgram, forms.InteresUser]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["special_abilities"] = SpecialAbilitiesModel.objects.all()
        context["profiles"] = ProfileModel.objects.all()
        context['news'] = PostModel.objects.all().order_by('-date')[:8]
        context["partners"] = models.PartnersModel.objects.all()   
        return context

    def form_valid(self, form):
        category = self.get_context_data()["page"]
        form.send_message(title=category)
        try:
            form.save(page="Заявка на поступление")
        except TypeError:
            form.save()

    
class EnrolleeView(FormView):
    template_name = "main/enrollee.html"
    form_class = forms.InteresUser
    extra_context = {
        "title": "Абитуриентам"
    }
    
    def get_success_url(self):
        return self.request.path
    
    def form_valid(self, form):
        context = self.get_context_data()
        form = self.get_form()
        form.send_message(context["title"])
        form.save(context["title"])
        return super().form_valid(form)
   

class CommitteeView(FormView):
    template_name = "main/selection-committee.html"
    extra_context = {
        "title": "Приемная коммиссия"
    }
    form_class = forms.InteresUser
    
    def get_success_url(self):
        return  self.request.path
    
    def form_valid(self, form):
        context = self.get_context_data()
        form = self.get_form()
        form.send_message(context["title"])
        form.save(context["title"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["programs"] = ProfileModel.objects.all()
        context["quitions"] = models.QuestionModel.objects.all()
        return context


class HistoryView(TemplateView):
    extra_context = {
        "title": "История колледжа"
    }
    template_name = "main/history.html"

    
class TimetableView(TemplateView):
    extra_context = {
        "title": "Расписание"
    }
    template_name = "main/timetable.html"


class LiveView(TemplateView):
    extra_context = {
        "title": "Жизнь Университета"
    }
    template_name = "main/live.html"


class HonorView(ListView):
    template_name = "main/honor.html" 

    def get_queryset(self):
        return TeacherModel.objects.all()#.filter(rank=self.kwargs["status"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Почетные доктора"
        if self.kwargs["status"] == "professor":
            context["title"] = "Почетные профессора"

        return context


# class ContactView(utils.FormListView):
#     template_name = "main/contact.html"
#     extra_context = {
#         "title": "Контакты"
#     }
    

#     def get_queryset(self):
#         page = self.extra_context["title"]   
#         return PagesModel.objects.all()
        
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
    
#     def form_valid(self, form):
#         f
#         return super().form_valid(form)

    
class ContactView(utils.FormListView):
    context_object_name = "faculties"

    template_name = "main/contact.html"
    extra_context = {
        "title": "Контакты",
        "go_to": forms.InteresUser(),
        "email": "123"
    }
    forms = [ forms.InteresUser ]

    def get_queryset(self, *args, **kwargs):
        self.object_list = PagesModel.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class QualityAdvice(TemplateView):
    template_name = "main/quality-advice.html"
    extra_context = {
        "title": "Совет по качеству"
    }
