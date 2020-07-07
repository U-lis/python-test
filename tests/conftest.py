import pytest

import app
from python_test.db import db


@pytest.fixture(scope="module")
def client():
    with app.app.test_client() as client:
        with app.app.app_context():
            db.create_all()
        yield client
        db.drop_all()
