from django.urls import path
from App import views

#Static Purpose
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.HomeView,name='Myhome'),
    path('home/',views.IndexView,name='home'),
    path('display/',views.PostView,name='display'),
    path('post/<str:pk>/',views.GetPostById,name='getpostbyid'),
    path('post<str:pk>/',views.DeletePost,name='delete'),
    path('createpost/',views.CreatePost,name='createpost'),
    path('post/<str:pk>/edit',views.UpdatePost,name='updatepost'),
    path('contact/',views.ContactUsPage,name='contact'),
    path('send',views.SendMail,name="send"),
    path('loginpage/',views.LoginPage,name='loginpage'),
    path('login/',views.LoginView,name='login'),
    path('logout/',views.LogoutView,name='logout'),
    path('registerpage/',views.RegisterPage,name='registerpage'),
    path('resister/',views.RegisterView,name='register'),
    path('myaccountpage/',views.MyAccountPage,name='myaccountpage'),
    path('myaccount/',views.MyAccountView,name='myaccount'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)