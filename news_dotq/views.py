from django.shortcuts import render
from .forms_mail import SendEmail
from django.http import HttpResponse, HttpResponseRedirect
#class base view
from django.views import View
from django.contrib.auth import decorators
from django.contrib.auth.mixins import LoginRequiredMixin

#func base view
# @decorators.login_required(login_url='../../login')
# def onEmail(req):
#     return render(req, 'news_dotq/email.html', {'mailOnEmail': SendEmail()})


#class base view
class OnEmail(LoginRequiredMixin, View):
    login_url = '../../login'

    def get(self, req):
        return render(req, 'news_dotq/email.html',
                      {'mailOnEmail': SendEmail()})


#func base view
# def onProcessView(req):
#     if req.method == 'POST':
#class base view
class OnProcessView(View):
    def post(self, req):
        arg_form = SendEmail(req.POST)
        if arg_form.is_valid():
            return render(req, 'news_dotq/view_email.html',
                          {'mailOnProcessView': arg_form})
        else:
            return HttpResponse(
                'Email form KO validate!!!'
            )  #mail="1@1.1" thì sẽ hiện ERR này (chứ KO bắt ở FE)

    # else:
    #     return HttpResponse('KO phải POST method!!!')
