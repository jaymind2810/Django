from django import forms
from .models import Students


class StudentsForm(forms.ModelForm):
    # each field would be mapped as an input field in HTML

    gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    address = forms.CharField(widget=forms.Textarea)
    roll_number = forms.IntegerField(widget=forms.TextInput)
    available_join = forms.DateField(widget=forms.SelectDateWidget)
    available = forms.BooleanField()
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender)

    class Meta:
        model = Students
        fields = "__all__"
        exclude = ["user"]


    def clean(self):

        # data from the form is fetched using super function
        super(StudentsForm, self).clean()

        # available = self.cleaned_data.get('available')

        mobile = self.cleaned_data.get('mobile')

        # conditions to be met for the username length
        if len(mobile) < 8:
            self._errors['mobile'] = self.error_class([
                'Minimum 8 characters required'])

        # return any errors if found
        return self.cleaned_data



