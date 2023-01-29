from django.db import models
from django.contrib.auth.models import User
from PIL import Image


MALE = 'MALE'
FEMALE = 'FEMALE'
OTHER = 'OTHER'
CHOICES = (
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other')
)

TYPE_ACCOUNT = (
    ('full', 'All inclusive'),
    ('free', 'Free package')
)
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('User photo', default='defaultUser.png', upload_to='user_images')
    sex = models.CharField(max_length=6, choices=CHOICES, default='MALE')
    my_bool = models.BooleanField(default='False', verbose_name=u'We use cookie on this site. I understand')
    account_type = models.CharField(choices=TYPE_ACCOUNT, default='free', max_length=30)

    def __str__(self):
        return f'User profile {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 250:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
