from django.contrib import admin
from .models import Project, JMF, QCReport, CoreReadings, NightlyReadings



# Register your models here.
admin.site.register(Project)
admin.site.register(JMF)
admin.site.register(CoreReadings)
admin.site.register(QCReport)
admin.site.register(NightlyReadings)