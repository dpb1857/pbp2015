
# Find pylint codes at: http://pylint-messages.wikidot.com/all-codes
# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=superfluous-parens

from django.urls import path

from data import views


urlpatterns = [
    path('controls/', views.ControlList.as_view()),
    path('controls/<int:pk>/', views.ControlDetail.as_view()),
    path('riders/', views.RiderList.as_view()),
    path('riders/<int:pk>/', views.RiderDetail.as_view()),
    path('timestamps/', views.TimestampList.as_view()),
    ]
