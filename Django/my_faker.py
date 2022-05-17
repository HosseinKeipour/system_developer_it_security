import imp
from faker import Faker 
import os 
import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_two.settings')
# django.setup()

# from AppTwo.models import Web

fake = Faker('it_IT')
# topic_fake = fake.text()

for _ in range(5):

    print(fake.text())
    print(fake.name())


