"""Tests for the calc CLI application.

This module demonstrates how to unit test Click commands using pytest and
click.testing.CliRunner.

Key point: The command functions are defined in calc.py, NOT in this test file.
This separation is important — it mirrors real projects where the CLI app lives
in its own module and tests import it. The confusion in issue #1119 came from
docs that appeared to nest the command inside the test; this example shows the
correct pattern.
"""

from click.testing import CliRunner

from calc import cli


def test_add():
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "2", "3"])
    assert result.exit_code == 0
    assert result.output == "5.0\n"


def test_sub():
    runner = CliRunner()
    result = runner.invoke(cli, ["sub", "10", "4"])
    assert result.exit_code == 0
    assert result.output == "6.0\n"


def test_mul():
    runner = CliRunner()
    result = runner.invoke(cli, ["mul", "3", "7"])
    assert result.exit_code == 0
    assert result.output == "21.0\n"


def test_div():
    runner = CliRunner()
    result = runner.invoke(cli, ["div", "20", "4"])
    assert result.exit_code == 0
    assert result.output == "5.0\n"


def test_div_by_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ["div", "10", "0"])
    assert result.exit_code != 0
    assert "Cannot divide by zero" in result.output


def test_invalid_args():
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "not-a-number", "5"])
    assert result.exit_code != 0
    assert "Invalid value" in result.output


def test_no_args():
    runner = CliRunner()
    result = runner.invoke(cli, [])
    assert result.exit_code != 0
    assert "Usage:" in result.output