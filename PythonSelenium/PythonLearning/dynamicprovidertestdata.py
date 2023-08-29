from faker import Faker
from faker.providers import DynamicProvider
from openpyxl import Workbook

fake= Faker()
names = [fake.unique.first_name() for i in range(500)]
print(names)
assert len(set(names)) == len(names)
print(len(set(names)) == len(names))
