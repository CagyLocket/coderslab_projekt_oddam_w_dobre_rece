from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views as cv


app_name = 'charity'


urlpatterns = [
    path('', cv.LandingPage.as_view(), name="landing-page"),
    path('add_donation/', cv.AddDonation.as_view(), name="add-donation"),
    # path('login/', cv.Login.as_view(), name="login"),
    path('login/', cv.LoginView.as_view(), name="login"),
    path('logout/', cv.LogoutView.as_view(), name="logout"),
    path('register/', cv.Register.as_view(), name="register"),
    path('reset_password/', cv.ResetPassword.as_view(), name="reset-password"),
    path('user_profile/', cv.UserProfile.as_view(), name="user-profile"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

