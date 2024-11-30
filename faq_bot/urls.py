from django.urls import path
from .views import FAQListView,query_view

urlspatterns=[
    path('faqs/',FAQListView.as_view(),name='faq-list'),
    path('query/',query_view,name='query-view'),

]