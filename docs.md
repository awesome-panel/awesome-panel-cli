# `awesome-panel-cli`

**Usage**:

```console
$ awesome-panel-cli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `autoformat`
* `build`
* `create`
* `examples`: Creates a folder with examples from the...
* `hello`: Serves the examples from the source...
* `release`
* `test`

## `awesome-panel-cli autoformat`

**Usage**:

```console
$ awesome-panel-cli autoformat [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `all`: Runs autoflake, isort and black
* `autoflake`: Runs autoflake to remove unused imports on...
* `black`: Runs black to autoformat all .py files...
* `isort`: Runs isort to sort all imports in all .py...

### `awesome-panel-cli autoformat all`

Runs autoflake, isort and black

**Usage**:

```console
$ awesome-panel-cli autoformat all [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `awesome-panel-cli autoformat autoflake`

Runs autoflake to remove unused imports on all .py files recursively

**Usage**:

```console
$ awesome-panel-cli autoformat autoflake [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `awesome-panel-cli autoformat black`

Runs black to autoformat all .py files recursively

**Usage**:

```console
$ awesome-panel-cli autoformat black [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `awesome-panel-cli autoformat isort`

Runs isort to sort all imports in all .py files recursively

**Usage**:

```console
$ awesome-panel-cli autoformat isort [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `awesome-panel-cli build`

**Usage**:

```console
$ awesome-panel-cli build [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `package`: Builds the python package

### `awesome-panel-cli build package`

Builds the python package

**Usage**:

```console
$ awesome-panel-cli build package [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `awesome-panel-cli create`

**Usage**:

```console
$ awesome-panel-cli create [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `app`: Creates a new app file in the current working...
* `binder`: Populates the .binder folder
* `github-actions`: Populates the .github folder
* `license`: Creates a new license file in the project...
* `notebook`: Creates a new notebook file in the current...
* `project`: Creates a new best practice python project...
* `view`: Creates a new view file in the current...
* `widget`: Creates a new widget file in the current...

### `awesome-panel-cli create app`

Creates a new app file in the current working directory

Args:
    name: The name of an reference app. Defaults to 'hello_world'.

**Usage**:

```console
$ awesome-panel-cli create app [OPTIONS] [NAME]:[altair|cross_filtering|hello_world|streaming_indicators]
```

**Arguments**:

* `[NAME]:[altair|cross_filtering|hello_world|streaming_indicators]`: [default: hello_world]

**Options**:

* `--help`: Show this message and exit.

### `awesome-panel-cli create binder`

Populates the .binder folder

**Usage**:

```console
$ awesome-panel-cli create binder [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `awesome-panel-cli create github-actions`

Populates the .github folder

**Usage**:

```console
$ awesome-panel-cli create github-actions [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `awesome-panel-cli create license`

Creates a new license file in the project root.

Args:
    name: The name of the license. Defaults to 'MIT'.

**Usage**:

```console
$ awesome-panel-cli create license [OPTIONS] [NAME]:[mit]
```

**Arguments**:

* `[NAME]:[mit]`: [default: mit]

**Options**:

* `--help`: Show this message and exit.

### `awesome-panel-cli create notebook`

Creates a new notebook file in the current working directory

Args:
    name: The name of an reference notebook. Defaults to 'introduction'.

**Usage**:

```console
$ awesome-panel-cli create notebook [OPTIONS] [NAME]:[introduction|getting_started]
```

**Arguments**:

* `[NAME]:[introduction|getting_started]`: [default: introduction]

**Options**:

* `--help`: Show this message and exit.

### `awesome-panel-cli create project`

Creates a new best practice python project for developing data apps

This will create a new project in a subfolder of the current directory.

This includes a virtual environment, a pyproject.toml file, a starter apps/app.py file,
a starter tests/test_hello.py file and more

**Usage**:

```console
$ awesome-panel-cli create project [OPTIONS]
```

**Options**:

* `--virtual-env / --no-virtual-env`: [default: True]
* `--help`: Show this message and exit.

### `awesome-panel-cli create view`

Creates a new view file in the current working directory

A view is just a function returning some object that Panel can display.

Args:
    name: The name of a reference view. Defaults to 'view'.
    example: If True the file generated contains a detailed example

**Usage**:

```console
$ awesome-panel-cli create view [OPTIONS] [NAME]:[view|html]
```

**Arguments**:

* `[NAME]:[view|html]`: [default: view]

**Options**:

* `--help`: Show this message and exit.

### `awesome-panel-cli create widget`

Creates a new widget file in the current working directory

A widget is a Parameterized Class with a `value` parameter. You can set the value. The value
can change when the user interacts with the widget.

Args:
    name: The name of a reference widget. Defaults to 'viewer'.
    example: If True the file generated contains a detailed example

**Usage**:

```console
$ awesome-panel-cli create widget [OPTIONS] [NAME]:[viewer]
```

**Arguments**:

* `[NAME]:[viewer]`: [default: viewer]

**Options**:

* `--example / --no-example`: [default: False]
* `--help`: Show this message and exit.

## `awesome-panel-cli examples`

Creates a folder with examples from the source repository.

**Usage**:

```console
$ awesome-panel-cli examples [OPTIONS] [SOURCE]
```

**Arguments**:

* `[SOURCE]`: [default: awesome-panel-cli]

**Options**:

* `--help`: Show this message and exit.

## `awesome-panel-cli hello`

Serves the examples from the source repository.

**Usage**:

```console
$ awesome-panel-cli hello [OPTIONS] [SOURCE]
```

**Arguments**:

* `[SOURCE]`: [default: awesome-panel-cli]

**Options**:

* `--port INTEGER`: [default: 5007]
* `--help`: Show this message and exit.

## `awesome-panel-cli release`

**Usage**:

```console
$ awesome-panel-cli release [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `package`: Release the Package to pypi Args: version:...

### `awesome-panel-cli release package`

Release the Package to pypi

Args:
    version: The version to upload, for example '0.1.0'.
    test: If True releases to test pypi. Defaults to False.

**Usage**:

```console
$ awesome-panel-cli release package [OPTIONS] VERSION
```

**Arguments**:

* `VERSION`: [required]

**Options**:

* `--test / --no-test`: [default: False]
* `--help`: Show this message and exit.

## `awesome-panel-cli test`

**Usage**:

```console
$ awesome-panel-cli test [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `all`: Runs all autoformatting and tests Arguments:...
* `bandit`: Runs Bandit the security linter from PyCQA.
* `mypy`: Runs mypy on all .py files recursively to...
* `pylint`: Runs Pylint (linter) on all .py files...
* `pytest`: Runs Pytest to identify failing tests Keyword...
* `show`: Opens a browser with the test coverage...

### `awesome-panel-cli test all`

Runs all autoformatting and tests

Arguments:
    fast {bool} -- If True tests marked slow will not be
        run. (default: False)
    report {bool} -- If True test reports will be generated in the test_results
        folder. (default: False)

**Usage**:

```console
$ awesome-panel-cli test all [OPTIONS]
```

**Options**:

* `--fast / --no-fast`: [default: False]
* `--report / --no-report`: [default: False]
* `--help`: Show this message and exit.

### `awesome-panel-cli test bandit`

Runs Bandit the security linter from PyCQA.

Args:
    report (bool, optional): If True an xml report will be created. Defaults to False.

**Usage**:

```console
$ awesome-panel-cli test bandit [OPTIONS]
```

**Options**:

* `--report / --no-report`: [default: False]
* `--help`: Show this message and exit.

### `awesome-panel-cli test mypy`

Runs mypy on all .py files recursively to identify type errors

Arguments:
    files {string} -- A space separated list of files and folders to lint
    report (bool, optional): If True an xml report will be created. Defaults to False.

**Usage**:

```console
$ awesome-panel-cli test mypy [OPTIONS]
```

**Options**:

* `--report / --no-report`: [default: False]
* `--help`: Show this message and exit.

### `awesome-panel-cli test pylint`

Runs Pylint (linter) on all .py files recursively to identify coding errors

Arguments:
    files {string} -- A space separated list of files and folders to lint
    report (bool, optional): If True an xml report will be created. Defaults to False.

**Usage**:

```console
$ awesome-panel-cli test pylint [OPTIONS]
```

**Options**:

* `--report / --no-report`: [default: False]
* `--help`: Show this message and exit.

### `awesome-panel-cli test pytest`

Runs Pytest to identify failing tests

Keyword Arguments:
    root_dir {str} -- The directory from which to run the tests
    test_files {str} -- A space separated list of folders and files to test. (default: {'tests})
    fast {bool} -- If True tests marked slow will not be
        run. (default: False)
    report {bool} -- If True test reports will be generated in the test_results
        folder. (default: False)

**Usage**:

```console
$ awesome-panel-cli test pytest [OPTIONS]
```

**Options**:

* `--fast / --no-fast`: [default: False]
* `--test-files TEXT`: [default: tests]
* `--report / --no-report`: [default: False]
* `--pdb / --no-pdb`: [default: False]
* `--help`: Show this message and exit.

### `awesome-panel-cli test show`

Opens a browser with the test coverage results

**Usage**:

```console
$ awesome-panel-cli test show [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
