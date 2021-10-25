from django import forms

class createNewRegister(forms.Form):
    personName = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    age = forms.CharField(label="العمر", widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone = forms.CharField(label="رقم الهاتف", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="البريد الالكتروني", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    TYPES_OF_VACCINE = (
        ('فايزر', 'فايزر'),
        ('سبوتنيك', 'سبوتنيك'),
        ('سبوتنيك لايت', 'سبوتنيك لايت'),
        ('موديرنا', 'موديرنا'),
    )
    typeVaccine = forms.MultipleChoiceField(label="نوع اللقاح المطلوب", choices = TYPES_OF_VACCINE)
    TYPES_OF_SICK = (
        ('a', 'نعم'),
        ('b', 'لا'),
    )
    # TYPES_OF_SICK = (
    #    ('نعم'),
    #    ('لا')
    # )
    
    sickBefore = forms.MultipleChoiceField(choices = TYPES_OF_SICK)
    notes = forms.CharField(label="أي ملاحظات", widget=forms.TextInput(attrs={'class': 'form-control'}))

class signIn(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password = forms.PasswordInput()
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "type": "password"
    }))