from django.urls import path

from .views import *

urlpatterns = [
    path('about/', AboutApiView.as_view(), name='about'),
    path('excuse/', ExcuseApiView.as_view(), name='excuse'),
    path('commit_message/', CommitMessageApiView.as_view(), name='commit'),
    path('error_message/', ErrorMessageApiView.as_view(), name='error'),
]
