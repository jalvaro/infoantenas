import pytest
from flask import url_for


class TestApp:

    def test_ping(self, client):
        res = client.get(url_for('healthcheck'))
        assert res.status_code == 200
        assert res.json == {'status': 'healthy!'}
