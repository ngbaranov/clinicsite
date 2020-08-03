from django import forms
from django.contrib import admin
from cooldoctor.models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class TopmenuAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = TopMenu
        fields = '__all__'

class TopMenuAdmin(admin.ModelAdmin):
    form = TopmenuAdminForm

admin.site.register(Header)
admin.site.register(TopMenu, TopMenuAdmin)
admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Action)
admin.site.register(Discounts)
admin.site.register(Article)
