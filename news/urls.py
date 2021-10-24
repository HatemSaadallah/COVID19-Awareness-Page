from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView, name="starting-page"),
    path("news", views.AllNewsView.as_view(), name="news-page"),
    path("register", views.registerCase, name="register"),
    path("images", views.AllImages.as_view(), name="images"),
    path("login", views.Login, name="login"),
    path("logout", views.Logout, name="logout"),
    path("news/<slug:slug>", views.SingleNewView.as_view(), name="news-detail-page")
]
