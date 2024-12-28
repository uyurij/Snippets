from django.forms import ModelForm
from MainApp.models import Snippet

# Создаем форму из модели forms.py
class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']
