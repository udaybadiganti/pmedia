from django import forms
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()

class UserLogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)

            if not user:
                raise forms.ValidationError('This user does not exist.')

            if not user.check_password(password):
                raise forms.ValidationError("Entered password is invalid.")

            if not user.is_active:
                raise forms.ValidationError("This user is not in active")

        return super(UserLogInForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label = 'Enter email')
    email2 = forms.EmailField(label = 'confirm email')
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError('email must be same.')

        email_eq = User.objects.filter(email = email)

        if email_eq.exists():
            raise forms.ValidationError('This email already exist.')

        return super(UserRegisterForm, self).clean(*args, **kwargs)
