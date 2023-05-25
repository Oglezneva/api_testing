from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_register():
    res = api.register('eve.holt@reqres.in', 'TopSecret1')

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res.json())


def test_negative_register():
    res = api.negative_register('eve.holt@reqres.in')
    res_body = res.json()
    example = {
        "error": "Missing password"
            }
    assert res.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(res.json())

    assert res_body['error'] == 'Missing password'
    assert example == res_body
