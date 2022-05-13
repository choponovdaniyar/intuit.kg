from django.db import models
from django.urls import reverse

class ProfileModel(models.Model):
    EMPTY_FIELD = "Поле может быть пустым"
    
    key = models.BigIntegerField(default=1, blank=True)
    
    title = models.CharField(verbose_name="Название", max_length=250)
    logo = models.FileField(verbose_name="Логотип", upload_to="faculty/images/logo",
                            blank=True)
    slug = models.SlugField(verbose_name="Ссылка",  blank=True)
    
    education = models.ForeignKey(verbose_name="Образование", to="EducationModel",
                                    on_delete=models.CASCADE,
                                    related_name="education",
                                    default = 1)
    faculty = models.ForeignKey('FacultyModel', verbose_name="Факультет",
                                    related_name="faculty", on_delete=models.CASCADE, 
                                    default = 1,)

    edu_form = models.ForeignKey('EduFormModel', verbose_name="Форма обучения",
                                    related_name="eduform", on_delete=models.CASCADE, 
                                    default = 1)

    details = models.ManyToManyField('DetailModel', verbose_name="Детали",
                                    related_name="detail_profile", blank=True) 

    work_places = models.TextField(verbose_name="Места работы", 
                                    help_text=EMPTY_FIELD, null=True, blank=True)

    suitable = models.TextField(verbose_name="Подходит для кого",
                                    help_text=EMPTY_FIELD, null=True, blank=True)

    description = models.TextField(verbose_name="Описание")
    
    courses = models.ManyToManyField(to="CourseModel", verbose_name="Курсы",
                                        related_name="courses", blank=True)

    skills = models.ManyToManyField(verbose_name="Навыки",to="SkillModel",
                                    related_name="skills", blank=True)

    documents = models.ManyToManyField(to="DocumentModel", verbose_name="Документы",
                                        related_name="documents", blank=True)

    professions = models.ManyToManyField(to="ProfessionModel",verbose_name="Професии",
                                            related_name="professions", blank=True)

    
    class Meta:
        ordering = ("key",)
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

    def get_absolute_url(self):
        return reverse("faculty:profile", args=[self.faculty.slug,self.education.slug, 
                                                self.edu_form.slug, self.slug])

    def __str__(self):
        return self.title


class TeacherModel(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=250)
    slug = models.SlugField(verbose_name="Ссылка",  blank=True)
    
    STATUS_CHOISE = (
        ("1", "Преподаватель"),
        ("2", "Старший преподаватель"),
        ("3", "Кандитат наук"),
        ("4", "Профессор"),
        ("5", "Доцент")
    )
    status = models.CharField(verbose_name="Звание", choices=STATUS_CHOISE, default="1", max_length=20)

    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.FileField(verbose_name="Изображение", upload_to="faculty/images/teachers", blank=True)


    facebook = models.CharField(
        verbose_name="facebook", 
        help_text='Введите ссылку на профиль (не обязательное полое)', 
        max_length=100,
        blank=True)

    telegram = models.CharField(
        verbose_name="Телеграм", 
        help_text="Введите ссылку на профиль (не обязательное полое)",
        max_length=100,
        blank=True)

    instagram = models.CharField(
        verbose_name="Инстаграм", 
        help_text="Введите ссылку на профиль (не обязательное полое)", 
        max_length=100,
        blank=True)

    youtube = models.CharField(
        verbose_name="YouTube", 
        help_text="Введите ссылку на профиль (не обязательное полое)",
        max_length=100,
        blank=True)

    curriculum_vitae = models.FileField(
        verbose_name="Логотип", 
        upload_to="faculty/files/cv", 
        blank=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def get_absolute_url(self):
            return reverse("faculty:teachers", args=[self.slug])


    def __str__(self):
        return self.name


class FacultyModel(models.Model):
    STATUS_CHOICES = (
        ("middle", "среднее"),
        ("post", "высшее")
    )
    title = models.CharField(verbose_name="Название", max_length=250)
    slug = models.SlugField(verbose_name="Ссылка", max_length=250)
    status = models.CharField(verbose_name="Образование", choices=STATUS_CHOICES, default="post",
                                 max_length=20)
                
    logo = models.FileField(verbose_name="Логотип", upload_to="faculty/images/icons/faculty", 
                            blank=True)


    class Meta:
        ordering = ("id",)
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"

    def get_absolute_url(self):
        return reverse("faculty:faculty", args=[self.slug])

    def __str__(self):
        return self.title


class DocumentModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    description = models.TextField(verbose_name="Описание")
    document = models.FileField(verbose_name="Документ", 
                                    upload_to="faculty/images/documents",
                                    null=True, blank=True)

    class Meta:
        ordering = ("title",)
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title


class CourseModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    description = models.TextField(verbose_name="Описание")

    class Meta:
        ordering = ("title",)
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        if self.courses.all().count() > 0:
            el = self.courses.all()[0]
        else:
            el = ""
        return f"{el}/{self.title}"


class SkillModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    description = models.TextField(verbose_name="Описание")
    
    class Meta:
        ordering = ("title",)
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title


class ProfessionModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    description = models.TextField(verbose_name="Описание")
    salary = models.CharField(verbose_name="Зарплата", max_length=250)

    class Meta:
        ordering = ("title",)
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"
    
    def __str__(self):
        return self.title


class EduFormModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=300)
    slug = models.SlugField(verbose_name="Ссылка")
    description = models.TextField(verbose_name="Описание")
    icon = models.ForeignKey(to="DetailModel", verbose_name="Иконка",
                                on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ("pk",)
        verbose_name = "Форма обучения"
        verbose_name_plural = "Формы обучения"

    def __str__(self):
        return f"{self.icon.page.title}/{self.title}"


class EducationModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    subtitle = models.CharField(verbose_name="Заголовок", max_length=250,
                                blank=True)
    slug = models.SlugField(verbose_name="ссылка")
    description = models.TextField(verbose_name="Описание", default="Описание")
    teachers = models.ManyToManyField(to="TeacherModel", verbose_name="Преподаватели", 
                                        related_query_name="education",  blank=True)

    detail = models.ManyToManyField(to="DetailModel", verbose_name="Детали",
                                    related_name="detail_education")
    special_abilities = models.ManyToManyField(to="SpecialAbilitiesModel",
            verbose_name="Специальные вопросы",
            related_name="education_specialabilities")
    eduform = models.ManyToManyField(verbose_name="Форма обучения", to="EduFormModel",
                                        related_name="edu_form")
    info = models.ManyToManyField(verbose_name="Общая информация", to="DetailModel",
                                        related_name="info")
    documents = models.ManyToManyField(verbose_name="Документы", to="DocumentModel", 
                                        blank=True, related_name="education_document")
    

    class Meta:
        ordering = ("title",)
        verbose_name = "Образование"
        verbose_name_plural = "Образования"

    def get_absolute_url(self):
        return reverse('faculty:education', args = [self.slug])

    def __str__(self):
        return self.title

class PagesModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    slug = models.SlugField(verbose_name="Ссылка", max_length=250)

    class Meta:
        ordering = ("title",)
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title


class DetailModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=500)
    numeric = models.CharField(verbose_name="Число", max_length=250, blank=True)
    image = models.FileField(verbose_name="Иконка", upload_to="faculty/images/icons/detail",
                            null=True, blank=True)
    page = models.ForeignKey(verbose_name="Страница", to="PagesModel", null=True, blank=True,
                                on_delete=models.CASCADE, default=1)
    
    
    class Meta:
        ordering = ("title",)
        verbose_name = "Деталь"
        verbose_name_plural = "Детали"

    def __str__(self):
        return f"{self.page}/{self.numeric} {self.title}"


class SpecialAbilitiesModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    description = models.TextField(verbose_name="Описание", blank=True)
    details = models.ManyToManyField(verbose_name="Детали", blank=True,
                                        related_name="abilities_detail",
                                        to = "SpecialAbilitiesDetailModel")

    class Meta:
        ordering = ('title',)
        verbose_name = "Специальная возможность"
        verbose_name_plural = "Специальные возможности"
    
    def  __str__(self):
        return self.title

    
class SpecialAbilitiesDetailModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)

    class Meta:
        ordering = ('title',)
        verbose_name = "Деталь специальных возможностей"
        verbose_name_plural = "Детали специальных возможностей"
    
    def  __str__(self):
        return self.title

