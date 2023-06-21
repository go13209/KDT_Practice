from django import forms
from .models import Todo
import datetime

class TodoForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': '제목 입력'},
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={'class': 'my-content'},
        )
    )
    priority = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'min': 1, 'max': 5, 'value': 3},
        )
    )
    deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'value': datetime.datetime.now().strftime("%Y-%m-%d")},
        )
    )

    class Meta:
        model = Todo
        fields = '__all__'