import factory
from python_test.db import db
from python_test.models.user import User
from faker import Faker

fake = Faker()


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    name = fake.name()
    user_id = name.split(" ")[0]
    user_pw = factory.Faker("sentence")
