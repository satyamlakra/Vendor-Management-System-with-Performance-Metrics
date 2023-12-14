from django.contrib import admin
from django.urls import path
from  intro import views

urlpatterns = [
     path('api-token-auth/', views.CustomAuthToken.as_view()),
     path('api/vendors/', views.vpmview.as_view()),
     path('api/vendors/<int:vendor_id>/', views.vpmview.as_view()),
     path('api/vendors/<int:vendor_id>/performance/', views.pvpmview.as_view()),
     path('api/purchase_orders/', views.poview.as_view()),
     path('api/purchase_orders/<int:po_id>/', views.poview.as_view()),
     path('api/purchase_orders/<int:po_id>/acknowledge/', views.apoview.as_view()),
]
