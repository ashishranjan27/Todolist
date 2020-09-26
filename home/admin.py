from django.contrib import admin

# Register your models here.
#all below written manually
#after model created come here and register it
from home.models import Task


admin.site.register(Task)

#then now use coammand to makemigration and migrate and then 
#create superuser and id and password and then run server 