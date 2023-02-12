from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

# Set the name of the app for URL namespacing
app_name = 'polls'

# Define URL patterns for the polls app
urlpatterns = [
    # The root path maps to the IndexView
    path('', views.IndexView.as_view(), name='index'),
    # Path for question detail pages
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # Path for question results pages
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # Path for voting on a question
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# Add static file paths to URL patterns
urlpatterns += staticfiles_urlpatterns()
