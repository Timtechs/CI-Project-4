from .models import Comment, Image
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')


class RoomForm(forms.ModelForm):
    """Form for the upload request"""
    class Meta:
        model = Room
        fields = ('body', 'image')
