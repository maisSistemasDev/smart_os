from django.urls import path
from .views import CreateAccount, CurrentUser

app_name = 'authentication'
urlpatterns = [
   path('create/', CreateAccount.as_view(), name="create_user"),
   path('currentUser/', CurrentUser.as_view(), name="current-user")
   ] 