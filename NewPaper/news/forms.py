from django import forms
from django.core.exceptions import ValidationError


from .models import Post


class PostForm(forms.ModelForm):
   title = forms.CharField(min_length=4)
   class Meta:
       model = Post
       fields = ['title', 'author', 'PostCategory', 'text',]

   def clean(self):
       cleaned_data = super().clean()
       title = cleaned_data.get("title")
       text = cleaned_data.get("text")

       if title == text:
           raise ValidationError(
               "Описание не должно быть идентично названию."
           )

       return cleaned_data

#form = PostForm()

#article = Post.objects.get(pk=1)
#form = PostForm(instance=article)