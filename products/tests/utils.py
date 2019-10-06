from products.models import Category, SubCategory, Product


def category_create(name):
    """
    Creates Category Model object used
    by test case
    :param name: name of the object
    :return: Category object
    """
    return Category.objects.create(name=name)


def sub_category_create(name, category):
    """
    Creates SubCategory Model object used
    by test case
    :param name: name of the object
    :param category: Category object
    :return: SubCategory object
    """
    return SubCategory.objects.create(name=name, category=category)


def product_create(title,  categories, sub_categories, price=1000, in_stock_qty=5):
    """
    Creates SubCategory Model object used
    by test case
    :param title: name of the object
    :param price: price of the object
    :param in_stock_qty: in stock quantity of the object
    :param categories: Category object list
    :param sub_categories: SubCategory object list
    :return: Product object
    """
    product = Product.objects.create(title=title, price=price, in_stock_qty=in_stock_qty)

    product.categories.set(categories)
    product.sub_categories.set(sub_categories)
    return product