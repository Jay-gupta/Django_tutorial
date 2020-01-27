from django.db import models
from django.contrib.auth.models import User
#
from multiselectfield import MultiSelectField

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

#trial
class Price_form(models.Model):
    js_options = (('30','0-$400') ,('29','$400-$1000') ,('28','$1000 - $3000') ,('27','$3,000-$5,000') ,('26','$5,000-$10,000') ,('25','$10,000 - $25,000') ,('24','$25,000 - $50,000') ,('23','$25,000 - $50,000'),
    )
    job_size = MultiSelectField(choices = js_options)



def __str__(self):
  return self.user.username