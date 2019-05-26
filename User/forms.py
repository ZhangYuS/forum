from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        error_messages = {
            'username': {
                'require': "请输入用户名"
            },
            'password': {
                'require': "请输入密码"
            }
        }

    def create(self):
        instance = self.save(commit=False)
        instance.set_password(self.cleaned_data.get('password'))
        if not User.objects.exists():
            instance.is_superuser = True
        instance.save()
        return instance


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request, *args, **kwargs)
        self.fields['username'].label = "用户名"
        self.fields['password'].label = "密码"
        self.fields['username'].widget.attrs.update({'placeholder': '请输入邮箱'})
        self.fields['password'].widget.attrs.update({'placeholder': '请输入密码'})
