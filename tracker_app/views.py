from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientCreateForm
# Create your views here.
def home(request):
    context = {"name" : request.user}
    return render(request,"tracker_app/home.html", context)

def login_view(request):
  context = {
    "login_view": "active"
  }
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      # Add your code below:
      login(request, user)
      return redirect("home")
    else:
      return HttpResponse("invalid credentials")
  return render(request, "registration/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("home")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient

class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem

class CreateIngredient(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = 'tracker_app/ingredient_create_form.html'
    form_class = IngredientCreateForm


class CreateMenuItem(LoginRequiredMixin, CreateView):
    pass

class UpdateIngredient(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = 'tracker_app/ingredient_update_form.html'
    form_class = IngredientCreateForm

class UpdateMenuItem(LoginRequiredMixin, UpdateView):
    pass 

class DeleteIngredient(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "tracker_app/ingredient_delete_form.html"
    success_url = "/ingredient/list"

class DeleteMenuItem(LoginRequiredMixin, DeleteView):
    pass