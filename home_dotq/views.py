from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms_dotq import RegistrationForm
from django.views import View


# Create your views here.
def onIndex(req):
    #chỉ cần gọi đường dẫn bên trong folder 'templates', còn 'pages' KO phải foldername bắt buộc
    return render(req, 'pages/home_dotq.html')


def onContact(req):
    return render(req, 'pages/contact.html')


# xử lí 404!!!
#handler404 cần 2 args: (req, exc) nhưng handler500 chỉ cần 1:(req)
# def on404(req, exc):
#     return render(req, 'pages/404.html', {'msg': exc})
#=> code vầy ko bị phụ thuộc số args!
def on404(req, *args, **kwargs):
    return render(req, 'pages/404.html')


def onRegister(req):
    arg_form = RegistrationForm()
    if req.method == 'POST':
        arg_form = RegistrationForm(req.POST)
        if arg_form.is_valid():
            arg_form.save()
            return HttpResponseRedirect('/')
    return render(req, 'pages/register.html', {'form_json': arg_form})


class IsLogin(View):
    def get(self, req):
        if not req.user.is_authenticated:
            return HttpResponse('Chưa login!!!')
        else:
            return HttpResponse('Xin chào "%s"' % (req.user.username))
