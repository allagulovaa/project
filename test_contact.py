# -*- coding: utf-8 -*-
import pytest

class Group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

@pytest.fixture
def test_group():
    return Group(name="lozka", header="kolbasa", footer="spati")

def test_create_group(app, test_group):
    app.session.login("admin", "secret")
    app.group.create_group(test_group)
    assert app.group.is_group_created(test_group.name), "Группа не была создана"
    app.session.logout()

def test_create_contact(app):
    app.session.login("admin", "secret")
    app.session.logout()