from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, HiddenField, validators


class LoginForm(Form):
    '''渲染用户登录html表单'''
    userid = StringField('客户账号： ', [validators.DataRequired('账号必须输入')])
    password = PasswordField('客户密码： ', [validators.DataRequired('密码必须输入')])


class CustomerRegForm(Form):
    '''渲染用户注册html表单'''
    userid = StringField('客户账号： ', [validators.DataRequired('账号必须输入')])
    name = StringField('客户姓名： ', [validators.DataRequired('姓名必须输入')])
    password = PasswordField('客户密码： ', [validators.DataRequired('密码必须输入')])
    password2 = PasswordField('再次输入密码： ', [validators.EqualTo('password', message='两次必须输入一致')])
    # 验证日期的正则表达式 YYYY-MM-DD YY-MM-DD
    reg_date = r'^((((19|20)(([02468][048])|([13579][26]))-02-29))|((20[0-9][0-9])|(19[0-9][0-9]))-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))$'
    birthday = StringField('出生日期： ', [validators.Regexp(reg_date, message='输入的日期无效')])
    address = StringField('通讯地址：')
    phone = StringField('电话号码：')
