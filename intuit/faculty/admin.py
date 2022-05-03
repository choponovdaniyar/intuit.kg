from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.register(PagesModel)

@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": (("id"),)
        }),
        (None, {
            "fields": (("title", "slug"),)
        }),
        (None, {
            "fields": (("logo", "get_logo"),)
        }),
        (None, {
            "fields": (("faculty",),)
        }),
        (None, {
            "fields": (("education",),)
        }),
        (None, {
            "fields": (("edu_form",),)
        }),
        (None, {
            "fields": (("details"),)
        }),
        (None, {
            "fields": (( "description", "work_places", "suitable",))
        }),
        (None, {
            "fields": (( "teachers", "courses", "skills", "professions", "documents"))
        }),
        
        
    ]  
    readonly_fields = ["get_logo", "get_faculty_title", "id"]
    list_display = ["key", 'title',"get_logo", "edu_form", "education", "faculty"] 
    list_display_links = ["title"]
    search_fields = [ "id", "title"]
    list_filter = [ "faculty", "education", "edu_form" ]
    list_editable = ["key", "edu_form", "education", "faculty"]

    prepopulated_fields = {"slug": ["title"]}

    filter_horizontal = ["courses", "teachers", "skills", 
                            "documents", "professions", "details"]         
    list_per_page = 10
    save_on_top = True
    save_as = True

    def get_logo(self, object):
        if object.faculty:
            return mark_safe(f"<img src='{object.faculty.logo.url}' height=100>")
    
    def get_faculty_title(self,object):
        return object.faculty.title

        
    get_faculty_title = "Факультет"
    get_logo.short_description = "лого факультета"


@admin.register(EduFormModel)
class EduFormAdmin(admin.ModelAdmin):
    list_display = ["title_", "title", "get_page", 'get_icon']
    search_fields = [ "title"]
    prepopulated_fields = {"slug": ["title"]}

    def get_icon(self,object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.image.url}' height=100>")

    def get_page(self,object):
        if object.icon:
            return object.icon.page
    
    def title_(self,object):
        page = self.get_page(object)
        return f"{page}/{object.title}"
@admin.register(EducationModel)
class EducationAdmin(admin.ModelAdmin):
    list_display = [ 'title'] 
    search_fields = [ "title"]
    prepopulated_fields = {"slug": ["title"]}
    filter_horizontal = ["detail", "special_abilities", "eduform", "info", "documents"]



@admin.register(DetailModel)
class DetailAdmin(admin.ModelAdmin):
    list_display = ["id", "numeric",'title', "get_icon"]    
    list_display_links = ["id"]
    search_fields = [ "title", "numeric"]
    list_editable = ["numeric", "title"]
    list_filter = [ "title" ]
    fieldsets = [
        (None, {
            "fields": (("numeric", "title"),)
        }),
        (None, {
            "fields": (("page"),)
        }),
        (None, {
            "fields": (("image", "get_icon"),)
        })
    ]  
    readonly_fields = ["get_icon"]
    list_per_page = 20
    save_as = True

    
    def get_icon(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=80>")

    get_icon.short_description = "Иконка"



@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    search_fields   = [ "name" ]
    list_display = [ 'name', 'get_photo']
    list_filter = [ "name" ] 
    list_per_page = 20
    readonly_fields = ["get_photo"]


    def get_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=100>")
    get_photo.short_description = "Фото"


@admin.register(DocumentModel)
class DocumentAdmin(admin.ModelAdmin):
    search_fields = [ "title"]
    list_display = [ 'title', 'get_doc']
    readonly_fields = ["get_doc"]
    list_filter = [ "title" ] 
    
    list_per_page = 20

    def get_doc(self, object):
        if object.document:
            return mark_safe(f"<img src='{object.document.url}' height=100>")

    get_doc.short_description = "Документ"


@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = [ "title", 'get_profile' ]
    search_fields = [ "title", "get_profile"]
    list_filter =  [ "title" ] 
    list_per_page = 20


    def get_profile(self,object):
        if object.courses.all().count() > 0:
            el = object.courses.all()[0]
        else:
            el = ""
        return f"{el}"
    get_profile.short_description = "Направление"

@admin.register(SkillModel)
class SkillAdmin(admin.ModelAdmin):
    list_display = [ 'title']
    search_fields = [ "title"]
    list_filter = [ "title" ] 
    list_per_page = 20


@admin.register(ProfessionModel)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = [ 'title', "salary"]
    search_fields = [ "title"]
    list_filter = [ "title" ] 
    list_per_page = 20


@admin.register(SpecialAbilitiesModel)
class SpecialAbilitiesAdmin(admin.ModelAdmin):
    list_display = [ 'title']
    search_fields = [ "title"]
    list_filter = [ "title" ] 
    filter_horizontal = ['details']

    list_per_page = 20

@admin.register(FacultyModel)
class FacultyAdmin(admin.ModelAdmin):
    list_display = [ 'title', "status",  "get_logo"]
    list_editable = ["status"]
    search_fields = [ "title"]
    list_filter = [ "title" ] 
    prepopulated_fields = {"slug": ["title"]}
    list_per_page = 20
    readonly_fields = ["get_logo"]

    
    def get_logo(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' height=80>")

    get_logo.short_description = "Логотип"


@admin.register(SpecialAbilitiesDetailModel)
class SpecialAbilitiesDetailAdmin(admin.ModelAdmin):
    list = display = ["title"]
    list_per_page = 20