from django.contrib import admin
from .models import ModelFAQ
# Register your models here.
@admin.register(ModelFAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display={'question','asnwer'}