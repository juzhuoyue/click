# Click Unit Testing Example

This example demonstrates how to unit test Click commands using pytest and
`click.testing.CliRunner`.

## Layout

```
testing/
├── calc.py         # The CLI application (commands defined here)
├── test_calc.py    # Unit tests (import commands from calc.py)
├── pyproject.toml  # Project config with pytest dependency
└── README.md       # This file
```

## Why the command lives in a separate module from the test

This example directly addresses the confusion from [issue #1119](https://github.com/pallets/click/issues/1119).
The Click documentation in `docs/testing.md` shows the command in `hello.py` and
the test in `test_hello.py` — they are separate files. However, without a
runnable example in the `examples/` directory, some users mistakenly thought the
command function should be nested *inside* the test function.

**Correct pattern (used here):**
- `calc.py` defines the Click commands (`cli`, `add`, `sub`, `mul`, `div`)
- `test_calc.py` imports those commands: `from calc import cli`
- Tests invoke the imported command via `CliRunner`

**Incorrect pattern (what confused users):**
```python
# DON'T do this
def test_hello():
    @click.command()
    @click.argument('name')
    def hello(name):
        click.echo(f'Hello {name}!')
    
    runner = CliRunner()
    runner.invoke(hello, ['Peter'])
```

The command should be defined in your application code, not in the test. Tests
import and exercise the real application.

## Running the tests

```bash
# Install the example in editable mode with test dependencies
pip install --editable ".[test]"

# Run tests
pytest examples/testing
# or from within the directory:
cd examples/testing && pytest
```

Expected output:
```
test_calc.py::test_add PASSED
test_calc.py::test_sub PASSED
test_calc.py::test_mul PASSED
test_calc.py::test_div PASSED
test_calc.py::test_div_by_zero PASSED
test_calc.py::test_invalid_args PASSED
test_calc.py::test_no_args PASSED
```

## Running the CLI manually

```bash
pip install --editable .
calc add 2 3        # 5.0
calc mul 6 7        # 42.0
calc div 10 0       # Error: Cannot divide by zero
```