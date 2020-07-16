from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Biography(models.Model):
    about_me = RichTextUploadingField(blank=True, null=True)
    experience = RichTextUploadingField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Biography'
        verbose_name_plural = "Biography"
    
    def __str__(self):
        return "About me"

class Technologies(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'technologies'
        verbose_name_plural = "Technologies - Programming Languages and Frameworks"

    def __str__(self):
        return self.name

class Projects(models.Model):
    project_name = models.CharField(max_length=255, blank=True, null=True)
    github_link = models.CharField(max_length=255, blank=True, null=True)
    short_description = RichTextUploadingField(blank=True)
    content = RichTextUploadingField(blank=True)
    preview_link = models.CharField(max_length=45, blank=True, null=True)
    image = models.ImageField(upload_to='project_images',blank=True, null=True)
    video = models.FileField(upload_to='project_videos', blank=True, null=True)
    technologies = models.ManyToManyField(Technologies)
    
    class Meta:
        managed = True
        db_table = 'projects'
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.project_name

class ContactMe(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message =models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'contact_me'
        verbose_name_plural = "Submited contact form"