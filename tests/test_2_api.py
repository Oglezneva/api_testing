from api.questions_api import api
from utils.assertions import Assert
from http import HTTPStatus


def test_2_api():
    res = api.list_users()

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res.json())


def test_3_api():
    res = api.single_user_not_found()

    assert res.status_code == HTTPStatus.NOT_FOUND
    Assert.validate_schema(res.json())


def test_4_api():
    res = api.single_user()
    res_body = res.json()

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res_body)

    assert res_body['data']['first_name'] == "Janet"
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
            }
    }
    assert example == res_body


def test_5_api():
    res = api.create('test', 'work')

    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == 'test'
    assert res.json()['job'] == 'work'

    assert api.delete_user(res.json()["id"]).status_code == HTTPStatus.NO_CONTENT










