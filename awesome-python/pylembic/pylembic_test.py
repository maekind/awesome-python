from os import path
from pytest import fixture

from pylembic.validator import Validator


@fixture
def with_alembic_config_path():
    return path.abspath(
        path.join(path.dirname(__file__), "migrations")
    )


def test_migrations(with_alembic_config_path):
    migration_validator = Validator(with_alembic_config_path)
    assert migration_validator.validate(verbose=True)
