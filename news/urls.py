from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("news", views.AllNewsView.as_view(), name="news-page"),
    path("register", views.RegisterForm.as_view(), name="register"),
    path("images", views.AllImages.as_view(), name="images"),
    path("news/<slug:slug>", views.SingleNewView.as_view(), name="news-detail-page")
]
