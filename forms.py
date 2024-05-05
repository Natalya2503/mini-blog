from django import forms
from .models import Post
from django.core.exceptions import ValidationError


# форма не связанная с моделью
# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200, label = 'Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), label = 'Контент')
#     author = forms.CharField(max_length=200, label='Автор', widget=forms.TextInput())

def check_blocker_symbols(title):
    blocker_symbols = ['<', '>', '=']
    for symbol in blocker_symbols:
        if symbol in title:
            raise ValidationError("Запрещенные символы")
    return title


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, 
                            validators=[check_blocker_symbols],
                            error_messages={'required': 'Без заголовка нельзя'},
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            label='Заголовок'
                            )
    content = forms.CharField(max_length=5000, 
                            error_messages={'required': 'Текст обязательно нужен'},
                            widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}),
                            label='Контент'
                            )
    author = forms.CharField(max_length=200, 
                            validators=[check_blocker_symbols],
                            error_messages={'required': 'Без автора - никак'},
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            label='Автор'
                            )
    class Meta:
        model = Post
        fields = ['title', 'content', 'author'] 

    def clean_content(self):
        content = self.cleaned_data['content']
        valid_string ='ёйцукенгшщзхъэждлорпавыфячсмитьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮЁ1234567890-!?$#@_'
        if not (set(content)<= set(valid_string)):
              raise ValidationError('Должны быть только русские символы, дефис и пробел')
        return content
           
