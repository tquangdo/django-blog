from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.onIndex),  #'...8000/'
    path('contact', views.onContact, name='contact'),  #'...8000/contact'
    path('register', views.onRegister, name='register'),
    path('is-login/', views.IsLogin.as_view()),
    # as_view() là generic view
    # "import views as auth_views" như kiểu <authComponent/> trong ReactJS
    path('login',
         auth_views.LoginView.as_view(template_name='pages/login.html'),
         name='login'),
    # LoginView, LogoutView là fix name
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout')
]  #Phải đúng convention, KO được là "urlPatterns"

#dùng authenticate()
# file "views.py"

# from django.contrib.auth import authenticate, login
# id / pw = req.POST['id/pw']
# my_user = authenticate(username=id, password=pw)
# if my_user is None:
#     return HttpResponse('User KO ton tai!!!')
# C1:
# return HttpResponse('username= %s, password= %s' % (id, pw))
# OR C2:
# login(req, my_user)
# return render(req, 'login_ok.html')