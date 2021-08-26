from django.contrib import admin

from .models import Education, Information, Work
# Register your models here.

class Info(admin.ModelAdmin):
    list_display = ('email', 'state')
    list_filter = ('state',)
    prepopulated_fields = {'slug': ('f_name', 'l_name', 'zip')}

admin.site.register(Information, Info)
admin.site.register(Education)
admin.site.register(Work)

#username: jasmeen
#password: jasmeen