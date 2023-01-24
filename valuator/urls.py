from django.urls import path

from . import views

urlpatterns = [
    path("", views.search, name="search"),
    path("search-results", views.SearchResultsView.as_view(), name="search-results"),
    path("details/", views.BottleDetailsView.as_view(), name="bottle-details"),
    path("trending/", views.trending, name="trending"),
    path("trending/bottle_details_trending/<str:mid>/",views.bottle_details_trending, name="bottle-details-trending"),
    path("popular/",views.popular, name="popular"),
    path("popular/search-results/<str:popular>/", views.search_results_popular, name="search-results-pop"),
    path("spinner/", views.PostTemplateView.as_view(), name="spinner-view"),
]