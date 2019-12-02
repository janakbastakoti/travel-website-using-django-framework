from django import forms
from .models import Blog

class CreateBlog(forms.ModelForm):
    name        = forms.CharField()
    topic       = forms.CharField()
    # img         = forms.CharField(required=False,widget=forms.ImageField(attrs={
    #                                                     'placeholder':'upload image',
    #                                                             }))
    discription = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder':'discription',

                                      }
                                  ))
    date        = forms.IntegerField()
    class Meta:
        model = Blog
        fields = [
            'name',
            'topic',
            # 'img',
            'discription',
            'date',
        ]

class RawCreate(forms.Form):
    name        = forms.CharField()
    topic       = forms.CharField()
    # img         = forms.CharField(required=False,widget=forms.ImageField(attrs={
    #                                                     'placeholder':'upload image',
    #                                                             }))
    discription = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder':'discription',

                                      }
                                  ))
    date        = forms.IntegerField()