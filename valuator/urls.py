from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from . import views

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.search, name="search"),
    path("search-results", views.SearchResultsView.as_view(), name="search-results"),
    path("details/", views.BottleDetailsView.as_view(), name="bottle-details"),
    path("trending/", views.trending, name="trending"),
    path("trending/bottle_details_trending/<str:mid>/",views.bottle_details_trending, name="bottle-details-trending"),
    path("popular/",views.popular, name="popular"),
    path("popular/search-results/<str:popular>/", views.search_results_popular, name="search-results-pop"),
    path("spinner/", views.PostTemplateView.as_view(), name="spinner-view"),
    path("login", LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name='logout'),
    path("register", views.register, name="register"),
    path("password-change/", PasswordChangeView.as_view(), name="password-change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
]