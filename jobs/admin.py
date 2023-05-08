from django.contrib import admin
from .models import Jobs,Personal,Blog,Author,Entry

# Register your models here.
admin.site.register(Jobs)
admin.site.register(Personal)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
