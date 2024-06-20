from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    path('categories/<slug:category_slug>', views.product_list, name="products_by_category"),
    path('<slug:category_slug>/<int:product_id>', views.product_detail, name="product_detail"),
    # New URL pattern for adding a review
    path('<int:product_id>/add_review/', views.add_review, name="add_review"),
]
