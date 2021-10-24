from django import forms

class createNewRegister(forms.Form):
    personName = forms.CharField(label="الاسم ثلاثي", max_length=255)

    age = forms.IntegerField(label="العمر")

    phone = forms.CharField(label="رقم الهاتف", max_length=255)
    email = forms.EmailField(label="البريد الالكتروني", max_length=255)
    TYPES_OF_VACCINE = (
        ('1', 'فايزر'),
        ('2', 'سبوتنيك'),
        ('3', 'سبوتنيك لايت'),
        ('4', 'موديرنا'),
    )
    typeVaccine = forms.MultipleChoiceField(label="نوع اللقاح المطلوب", choices = TYPES_OF_VACCINE)
    TYPES_OF_SICK = (
        ('a', 'نعم'),
        ('b', 'لا'),
    )
    sickBefore = forms.MultipleChoiceField(choices = TYPES_OF_SICK)
    notes = forms.CharField(label="أي ملاحظات")

class signIn(forms.Form):
    username = forms.CharField(max_length=255)
    # password = forms.PasswordInput()
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        "type": "password"
    }))