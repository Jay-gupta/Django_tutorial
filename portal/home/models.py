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
class Job_Size(models.Model):
    js_options = (('30','0-$400'), ('29','$400-$1000'), ('28','$1000 - $3000'), ('27','$3,000-$5,000'), ('26','$5,000-$10,000'), ('25','$10,000 - $25,000'), ('24','$25,000 - $50,000'), ('23','$25,000 - $50,000'),)
    job_size = MultiSelectField(choices = js_options)

class Company_Size(models.Model):
    cs_options = (('30','0-$400'), ('29','$400-$1000'), ('28','$1000 - $3000'), ('27','$3,000-$5,000'), ('26','$5,000-$10,000'), ('25','$10,000 - $25,000'), ('24','$25,000 - $50,000'), ('23','$25,000 - $50,000'),)
    company_size = MultiSelectField(choices = cs_options)

class Priority(models.Model):
    p_options = (('15','1.1'), ('10','1'), ('5','2'), ('0','3'),)
    priority = MultiSelectField(choices = p_options)

class Turnaround_Time(models.Model):
    tt_options = (('10','Very Quck'), ('5','Quick'), ('0','Average'),)
    turnaround_time = MultiSelectField(choices = tt_options)

class Requirement_Specification(models.Model):
    rs_options = (('100','Hardly any definition'), ('40','Roughly Defined'), ('20','Clearly Defined'), ('10','Clearly defined with Disclaimer'), ('0','Manmonth'),)
    req_spec = MultiSelectField(choices = rs_options)

class Credit_Days(models.Model):
    cd_options = (('0','Advance Payment'), ('1.0','21 days Credit'), ('2.0','30 days Credit'), ('2.5','45 days Credit'), ('3','60 days Credit'),)
    priority = MultiSelectField(choices = cd_options)

class Manpower_Util(models.Model):
    mu_options = (('-10','110'), ('0','90'), ('10','80'), ('20','70'), ('25','60'),)
    manpower_util = MultiSelectField(choices = mu_options)


def __str__(self):
  return self.user.username