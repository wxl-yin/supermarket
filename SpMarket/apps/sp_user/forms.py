from django import forms

from sp_user.models import SpUser

"""
    普通的form
    
    
    modelform

"""


class RegisterModelForm(forms.ModelForm):
    """注册表单, 验证"""
    # 单独添加字段
    password1 = forms.CharField(max_length=16,
                                min_length=6,
                                error_messages={
                                    'required': '密码必填',
                                    'max_length': '密码长度不能大于16个字符',
                                    'min_length': '密码长度必须大于6个字符',
                                }
                                )
    password2 = forms.CharField(error_messages={'required': "确认密码必填"})

    class Meta:
        model = SpUser
        # 需要验证的字段
        fields = ['phone', ]

        error_messages = {
            "phone": {
                "required": "手机号码必须填写!"
            }
        }

    # 单独清洗(验证)
    def clean_password2(self):
        # 验证两个密码是否一致
        pwd1 = self.cleaned_data.get('password1')
        pwd2 = self.cleaned_data.get('password2')

        if pwd1 and pwd2 and pwd1 != pwd2:
            # 确认密码错误
            raise forms.ValidationError("两次密码输入不一致!")
        return pwd2

    def clean_phone(self):
        # 验证手机号码是否唯一
        phone = self.cleaned_data.get('phone')
        rs = SpUser.objects.filter(phone=phone).exists()  # 返回bool
        if rs:
            raise forms.ValidationError("手机号码已经被注册")
        return phone
