from django import forms
from django.core.exceptions import ValidationError

from  .models import UserInfo
# myapp/forms.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['UserName',
                  'pwd',
                  'email',
                  ]
        labels = {
            'UserName': "请输入您的账号",
            'pwd':  "请输入您的密码",
            'email':  "请输入您的电子邮箱"
            }

    def clean_UserName(self):
        username = self.cleaned_data['UserName']
        if len(username) < 6 or len(username) > 120:
            raise ValidationError("用户名长度必须大于6位且小于120位")
        return username

    UserName = forms.CharField(
        error_messages={'required': '自定义的这个字段是必填项的消息'}
    )
    def clean_pwd(self):
        pwd = self.cleaned_data['pwd']
