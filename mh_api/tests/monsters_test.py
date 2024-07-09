import sys
from fastapi.testclient import TestClient
from mh_api.main import app

client = TestClient(app)


def test_links_get():
    res = client.get("/api/links")
    assert res.status_code == 200
    assert "Zinogre" in res.json()


def test_monster_all():
    res = client.get("/api/monsters")
    assert res.status_code == 200
    assert len(res.json()["items"]) == 50


def test_monster_pagination_works():
    res = client.get("/api/monsters?size=1")
    assert res.status_code == 200
    assert len(res.json()["items"]) == 1


def test_monster_not_exists404():
    non_existent_id = 66666666666666666666
    res = client.get(f"/api/monster/{non_existent_id}")
    assert res.status_code == 404
    assert res.json()["detail"] == f"No monster with id {non_existent_id}"


def test_resource_not_exists404():
    res = client.get("/not-exists-url")
    assert res.status_code == 404
    assert res.json()["detail"] == "Not Found"
