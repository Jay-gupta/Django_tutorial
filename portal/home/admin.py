from django.contrib import admin
from home.models import UserProfileInfo, User
from home.models import Job_Size, Company_Size, Priority, Turnaround_Time, Requirement_Specification, Credit_Days, Manpower_Util


# Register your models here.
admin.site.register(UserProfileInfo)

#trial
admin.site.register(Job_Size)
admin.site.register(Company_Size)
admin.site.register(Priority)
admin.site.register(Turnaround_Time)
admin.site.register(Requirement_Specification)
admin.site.register(Credit_Days)
admin.site.register(Manpower_Util)
