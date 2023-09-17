from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views as cv


app_name = 'charity'


urlpatterns = [
    path('', cv.LandingPage.as_view(), name="landing-page"),
    path('add_donation/', cv.AddDonation.as_view(), name="add-donation"),
    path('login/', cv.Login.as_view(), name="login"),
    path('register/', cv.Register.as_view(), name="register"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

