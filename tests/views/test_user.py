import json

import pytest

from python_test.db import db
from tests.factory.user import UserFactory


@pytest.fixture(scope="session")
def dummy_user():
    user = UserFactory()
    db.session.commit()
    return user


def test_login_page(client):
    resp = client.get("/user/login")
    assert resp.status_code == 200
    resp_data = resp.data.decode()
    assert '<input type="text" name="user_id">' in resp_data
    assert '<input type="password" name="user_pw">' in resp_data


class TestLogin:
    def test_success(self, client, dummy_user):
        resp = client.post("/user/login", data={"user_id": dummy_user.user_id, "user_pw": dummy_user.user_pw},
                           follow_redirects=True)
        assert resp.status_code == 200
        data = json.loads(resp.data.decode())
        assert data["ok"] is True
        assert data["title"] == f"Welcome {dummy_user.name}!"

    def test_user_not_found(self, client, dummy_user):
        resp = client.post("/user/login", data={"user_id": "WRONG_ID", "user_pw": dummy_user.user_pw},
                           follow_redirects=True)
        assert resp.status_code == 200
        data = json.loads(resp.data.decode())
        assert data["ok"] is False
        assert data["title"] == "User Not Found"

    def test_wrong_password(self, client, dummy_user):
        resp = client.post("/user/login", data={"user_id": dummy_user.user_id, "user_pw": "WRONG_PASSWORD"},
                           follow_redirects=True)
        assert resp.status_code == 200
        data = json.loads(resp.data.decode())
        assert data["ok"] is False
        assert data["title"] == "Wrong Password"
