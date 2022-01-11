from django import forms
from django.db.models import fields
from django.db.models.fields import Field
from .models import imge
class imgeform(forms.ModelForm):
    class Meta:
        model=imge
        fields=['img','price','des']
        



