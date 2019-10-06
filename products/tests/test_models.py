from django.contrib.auth import get_user_model
from django.test import TestCase

from products.models import Category, SubCategory, Product
from .utils import category_create, sub_category_create, product_create

User = get_user_model()


class TestCategoryModel(TestCase):
    """
    This class is for testing Category model
    """

    def setUp(self):
        self.user = User.objects.create_user(username='usertest', password='abc1234', email='usertest@example.com')

    def test_category_creation(self):
        """
        testing if Category object is being
        created properly
        """
        category1 = category_create("Casual")
        category2 = category_create("Formal")
        category_queryset = Category.objects.all()
        self.assertEqual(category_queryset.count(), 2)
        self.assertEqual(category_queryset.first(), category1)
        self.assertEqual(category_queryset.last(), category2)


class TestSubCategoryModel(TestCase):
    """
    This class is for testing SubCategory model
    """

    def setUp(self):
        self.user = User.objects.create_user(username='usertest', password='abc1234', email='usertest@example.com')

    def test_sub_category_creation(self):
        """
        testing if SubCategory object is being
        created properly
        """
        category = category_create("Casual")
        sub_category = sub_category_create(name='Shirt', category=category)
        sub_category_queryset = SubCategory.objects.all()

        self.assertEqual(sub_category_queryset.count(), 1)
        self.assertEqual(sub_category_queryset.first(), sub_category)


class TestProductModel(TestCase):
    """
    This class is for testing Product model
    """

    def test_product_creation(self):
        """
        testing if Product object is being
        created properly
        """
        category = category_create("Casual")
        sub_category = sub_category_create('shirt', category=category)
        product = product_create(title="Lee", categories=[category], sub_categories=[sub_category])
        product_queryset = Product.objects.all()
        #
        self.assertEqual(product_queryset.count(), 1)
        self.assertEqual(product.categories.all().count(), 1)
        self.assertEqual(Category.objects.first(), product.categories.first())