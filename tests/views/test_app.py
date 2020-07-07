import flask as fl


def test_ping(client):
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.data == "pong".encode()


def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data.decode() == fl.render_template("index.jinja2")
    assert "<!DOCTYPE html>" in resp.data.decode()
    assert "Hello World" in resp.data.decode()
