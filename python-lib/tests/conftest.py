import pytest
from fastapi import FastAPI
from typer import Typer


@pytest.fixture(scope="session")
def cli_app() -> Typer:
    from template_package import cli

    print("Create cli_app fixture")
    return cli.app


@pytest.fixture(scope="session")
def api_app() -> FastAPI:
    from template_package import api

    print("Create api_app fixture")
    return api.app
