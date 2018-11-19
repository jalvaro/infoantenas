import pytest

from app.myapp import create_app


@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    return app
