from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Category, Review

class ReviewTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a category
        self.category = Category.objects.create(name='Electronics', slug='electronics')

        # Create a product
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=9.99,
            category=self.category
        )

        # Create a review
        self.review = Review.objects.create(
            user=self.user,
            product=self.product,
            rating=5,
            comment='Great product!'
        )

    def test_review_content(self):
        # Test the review content
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.product, self.product)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, 'Great product!')

    def test_product_reviews(self):
        # Test that the product has the correct review
        reviews = self.product.review_set.all()
        self.assertIn(self.review, reviews)

    # Add more tests as needed for your application
