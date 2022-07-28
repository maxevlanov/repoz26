from requests import Session


def test_request():
    with Session() as session:
        response = session.post(
            url="http://localhost:8000/api/1/category/del",
            headers={"Authorization": "Bearer fe3a31a38f32149c8c465f3dd77981f292a1dca3c3af87b87edb413698291bfe"},
            json={"name": "category_test3", "parent_id": None}
        )
        print(response.status_code)
        print(response.json())

foo()