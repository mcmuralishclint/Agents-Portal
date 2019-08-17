from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from user import views

app_name = "user"
urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name =  'user/signin.html'), name='sign_in'),
    path('signout/', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='sign_out'),
	path('profile/<id>', views.profile, name="profile"),
	path('featured/', views.featured, name="featured"),
    #path('signup/', user_views.sign_up, name='sign_up'),

]
