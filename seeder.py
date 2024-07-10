import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()


from products.models import *
from django.contrib.auth.models import User

def seed_data():
    user = User.objects.first()

    for category in categories:
        Category.objects.create(
            name=category['name'],
            image=category['image'],
            author=category['author'],
            color=category['color'],
            created_at=datetime.datetime.now()
        )
    print('Successfully seeded data')

if __name__ == '__main__':
    seed_data()
