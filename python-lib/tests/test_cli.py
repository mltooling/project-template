#!/usr/bin/env python

from typer.testing import CliRunner

from template_package import cli

runner = CliRunner()


def test_cli() -> None:
    """Test the CLI."""
    result = runner.invoke(cli.app, ["hello", "foo"])
    assert result.exit_code == 0
    assert "foo" in result.stdout
