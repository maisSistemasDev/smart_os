from django.urls import path
from .views import OSView, FuncionarioView

app_name = 'core'
urlpatterns = [
   path('os/', OSView.as_view(), name="ordem_de_servico"),
   path('funcionarios/', FuncionarioView.as_view(), name="funcionarios")
   ] 