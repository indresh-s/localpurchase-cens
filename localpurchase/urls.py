from django.urls import path
from . import views

urlpatterns = [
    path('',views.add, name='index'),
    path('add/',views.add, name='add'),
    path('view-record/',views.index, name='view-record'),
    path('view-record/single-record',views.viewSingleRecord, name='single-record'),
    path('approval/',views.approval, name='approval'),
    path('bill-submission/',views.bill_submission, name='bill-submission'),
    path('bill-submission-list/',views.bill_submission_list, name='bill-submission-list')
]