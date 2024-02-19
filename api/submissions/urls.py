from django.urls import path
from submissions import views

urlpatterns = [
    path('submit-code/', views.SubmitCodeAPIView.as_view()),
    path('view-submissions/', views.ViewSubmissionsAPIView.as_view()),
    path('get-result/<str:task_id>', views.TaskStatusView.as_view()),
]
