from django.urls import path
from .views import add_review

urlpatterns = [
    # ... your other url patterns
    path('product/<int:product_id>/add_review/', add_review, name='add_review'),
]
