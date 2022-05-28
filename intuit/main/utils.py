from django.shortcuts import render
from django.views.generic.base import View, ContextMixin
from django.views.generic.list import ListView


from faculty.models import DetailModel, PagesModel

class FormsView(ContextMixin, View):
    '''
        Отображение для обработки нескольких форм
    '''
    template_name: str
    forms: list


    def get_success_template_name(self):
        return self.template_name

    def form_valid(self, form):
        return form
    
    def form_invalid(self, form):
        return form

    def validate(self, form):
        if form.is_valid():
            self.form_valid(form)
            return 1
        self.form_invalid(form)
        return 0

    def post(self, request, *args, **kwargs):
        for form in self.forms:
            if self.validate(form(request.POST)):
                break
        return render(request, self.get_success_template_name(), self.get_context_data())

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class SavePageMixin(View):
    def get(self, request, *args, **kwargs):
        page = self.get_context_data()["title"]
        PagesModel.objects.get_or_create(title=page)


class FormListView(SavePageMixin, ListView,FormsView):
    def get_queryset(self, *args, **kwargs):
        return self.object_list

    def get_context_data(self, **kwargs):
        self.get_queryset()
        contextF = ListView.get_context_data(self, **kwargs)
        context = FormsView.get_context_data(self, **kwargs)
        for el in contextF:
            context[el] = contextF[el]
        return context

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        for form in self.forms:
            if self.validate(form(request.POST)):
                break
        success_template = self.get_success_template_name()
        return render(request, success_template, self.get_context_data())
        
    def form_valid(self, form):
        category = self.get_context_data()["title"]
        form.send_message(title=category)
        try:
            form.save(page=category)
        except TypeError:
            form.save()