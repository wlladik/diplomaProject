from django.db import models
from django.urls import reverse

class Course(models.Model):
    #slug = id = 1...
    #slug, title, desc, image
    slug = models.SlugField('Unique name')
    title = models.CharField('Course name', max_length=120)
    desc = models.TextField('About course')
    image = models.ImageField("Image", default='default.png', upload_to='course_images') #install pillow for img
    is_free = models.BooleanField('Free?', default=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug':self.slug})

class Lesson(models.Model):
    #slug, title, desc, course, number, video_url
    slug = models.SlugField('Unique name lesson')
    title = models.CharField('Lesson name', max_length=120)
    desc = models.TextField('About lesson')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Which course?')
    number = models.IntegerField('Number of lesson')
    video = models.CharField('Video URL', max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})