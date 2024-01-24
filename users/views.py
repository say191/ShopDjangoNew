from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, View, UpdateView
from users.models import User
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm, UserForm
from random import randint
import smtplib
import os
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import render
from django.shortcuts import redirect


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        new_user.email_token = str(randint(10001, 99999))
        new_user.save()
        current_site = get_current_site(self.request)
        html_message = render_to_string(
            'users/verify_email.html',
            {
                'domain': current_site.domain,
                'email_token': new_user.email_token
            })
        message = MIMEMultipart()
        message['Subject'] = 'Confirming registration in Store'
        message.attach(MIMEText(html_message, 'plain'))
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=os.getenv('EMAIL_HOST'), password=os.getenv('PASSWORD_HOST'))
        connection.sendmail(
            from_addr=os.getenv('EMAIL_HOST'), to_addrs=new_user.email, msg=message.as_string())
        connection.close()
        return super().form_valid(form)


class EmailVerify(View):
    def get(self, request, email_token):
        try:
            user = User.objects.get(email_token=email_token)
            user.is_active = True
            user.save()
            return render(request, 'users/register_success.html')
        except User.DoesNotExist:
            return render(request, 'users/register_failed.html')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(randint(1, 9)) for _ in range(12)])
    message = MIMEMultipart()
    message['Subject'] = 'Reset password'
    message.attach(MIMEText(f"Your new password - {new_password}", 'plain'))
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=os.getenv('EMAIL_HOST'), password=os.getenv('PASSWORD_HOST'))
    connection.sendmail(
        from_addr=os.getenv('EMAIL_HOST'), to_addrs=request.user.email, msg=message.as_string())
    connection.close()
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('products:list'))
