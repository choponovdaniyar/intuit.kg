from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.mail import send_mail


from . import forms
from . import models
from faculty.models import SpecialAbilitiesModel, ProfileModel
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


def enrollee(request):
    context = {
        "consultation": forms.InteresUser(),
        "title": "Абитуриентам"
    }
    if request.method == 'POST':
        form = forms.InteresUser(request.POST)
        if form.is_valid():
            send_mail(
                '| intuit.kg | Консультатция', 
                get_message(request),
                EMAIL_HOST_USER, 
                [ EMAIL_HOST_USER ], 
                fail_silently=False
            )
            save_interesed_user(request, context["title"])
    return render(request, template_name = "main/enrollee.html", context=context)

        

def main(request):
    context = dict()
    context["title"] = "Главная"
    context["special_abilities"] = SpecialAbilitiesModel.objects.all()
    context["profiles"] = ProfileModel.objects.all()
    context["quiz"] = forms.ChoiceProgram()
    context["go_to"] = forms.InteresUser()
    context['news'] = PostModel.objects.all().order_by('-date')[:8]
    context["partners"] = models.PartnersModel.objects.all()
  
    if request.method == 'POST':
        form = forms.ChoiceProgram(request.POST)
        if form.is_valid():
            title = '| intuit.kg | Выбор программы'
            send_mail(
                title, 
                get_message(request),
                EMAIL_HOST_USER, 
                [ EMAIL_HOST_USER ], 
                fail_silently=False
            )
            form.save()
        else:
          form = forms.InteresUser(request.POST)
          if form.is_valid():
              title = '| intuit.kg | Запись на день открытых дверей'
              send_mail(
                  title, 
                  get_message(request),
                  EMAIL_HOST_USER, 
                  [ EMAIL_HOST_USER ], 
                  fail_silently=False
              )
              save_interesed_user(request, context["title"])
    return render(request, template_name="main/index.html", context=context)

    


def selection_committee(request):
    context = {
        "go_to": forms.InteresUser(),
        "title": "Абитуриентам",
        "programs": ProfileModel.objects.all()
    }
    if request.method == 'POST':
        form = forms.InteresUser(request.POST)
        if form.is_valid():
            send_mail(
                '| intuit.kg | Приемная коммисия', 
                get_message(request),
                EMAIL_HOST_USER, 
                [ EMAIL_HOST_USER ], 
                fail_silently=False
            )
            save_interesed_user(
                request, 
                context["title"]
            )
    return render(
        request, 
        template_name="main/selection-committee.html", 
        context=context
    )