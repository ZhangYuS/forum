from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        error_messages = {
            'username':{
                'require': "请输入用户名"
            },
            'password' : {
                'require' : "请输入密码"
            }
        }

    def create(self):
        instance = self.save(commit=False)
        instance.set_password(self.cleaned_data.get('password'))
        if not User.objects.exists():
            instance.is_superuser = True
        instance.save()
        return instance