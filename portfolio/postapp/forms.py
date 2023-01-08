from django import forms
from .models import Post,Comment

class Create_Post(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('creator',)


class Edit_Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('creator',)


class Add_Comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
