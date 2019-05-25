from django import forms
from testapp.models import Student

class StudentForm(forms.ModelForm):
    def clean_marks(self):
        print("hello")
        inputmarks = self.cleaned_data['marks']
        if inputmarks < 10:
            print("hello")
            raise forms.ValidationError('minimum marks should be 10')
        return inputmarks

    class Meta:
        model = Student
        fields = '__all__'
