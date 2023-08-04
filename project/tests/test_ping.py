# project/tests/test_ping.py


# from app import main


def test_ping(test_app):
    response = test_app.get("/ping")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"environment": "dev",
                               "ping": "pong!",
                               "testing": True}
