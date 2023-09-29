from django import forms
from .models import Cook


class CookCreateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ('username', 'password', 'first_name', 'years_of_experience')

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data.get('years_of_experience')
        if years_of_experience < 0:
            raise forms.ValidationError("Years of experience cannot be negative.")
        return years_of_experience
