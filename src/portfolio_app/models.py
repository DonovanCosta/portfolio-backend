from django.db import models

# Create your models here.
class Biography(models.Model):
    about_me = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Biography'
        verbose_name_plural = "Biography"

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
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
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
