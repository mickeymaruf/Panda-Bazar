from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.signin, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('activate/<uid>/<token>/', views.activate, name="activate"),

    path('submit_review/<slug:product_slug>/', views.submit_review, name="submit_review"),
]