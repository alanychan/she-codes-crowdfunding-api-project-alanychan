from django.urls import path
from . import views

urlpatterns = [
	path('projects/', views.ProjectList.as_view(), name='project-list'),
	path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('pledges/', views.PledgeList.as_view(), name='pledge-list'),
    path('projectupdates/', views.ProjectUpdatesList.as_view(), name='project-updates'),
]
