from django.contrib import admin
from .models import Record, Schedule, ClassRoster, Attendance, Grade

admin.site.register(Record)
admin.site.register(Schedule)
admin.site.register(ClassRoster)
admin.site.register(Attendance)
admin.site.register(Grade)
# Config: Django Admin Registry