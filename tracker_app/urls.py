from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ingredient/list', views.IngredientList.as_view(), name='ingredientlist'),
    path('ingredient/create', views.CreateIngredient.as_view(), name='ingredientcreate'),
    path('ingredient/update/<pk>', views.UpdateIngredient.as_view(), name='ingredientupdate'),
    path('ingredient/delete/<pk>', views.DeleteIngredient.as_view(), name='ingredientdelete'),
    path('accounts/login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]