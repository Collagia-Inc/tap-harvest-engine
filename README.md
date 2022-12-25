# tap-harvest-engine

## Overview

`tap-harvest-engine` is a Singer tap for HarvestEngine.

Built with the Meltano [SDK](https://gitlab.com/meltano/singer-sdk) for Singer Taps.

This repo has the following components:

- Source code
- Tests
- Misc configuration files (in the root directory)

#### Dependencies

This repo was built with python 3.7.9 on Mac OS 10.15.7
It uses `tox` and `poetry` [docs](https://python-poetry.org/).

- pip install tox
- pip install poetry
- poetry install

## Configuration

```
{
  "api_url": "http://localhost",
  "p_connection_pk": <int>
}
```

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-harvest-engine --about
```

### Source Authentication and Authorization

Currently there is no authentication and authorization required by the HE.

## Source code

Source code is stored in the `/tap_harvest_engine` folder

- client class - parent class for implementing HE specific client logic including: pagenation, filtering, url parameters, response parsing, etc.
- streams classes - contains all stream implementations. This includes: name, schema, replication keys, url, etc.
- tap class - class defines the requiremented singer configs and the streams supported by the discover process.

## Usage

You can easily run `tap-harvest-engine` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Tap Directly

```bash
tap-harvest-engine --version
tap-harvest-engine --help
tap-harvest-engine --config CONFIG --discover > ./catalog.json
```

## Tests

Test code is stored in the `/tests/tox_tests` folder.

Meltano's Singer SDK has built-in core tap tests `get_standard_tap_tests` which checks things like discovery, cli
functionality, auth, and does a full sync of streams.

These core tests were retro fitted for Collagia's small/medium/large testing pattern. The difference between medium and
large core tests in this context are that medium tests use the `responses` package to mock the API calls instead of
actually connecting like the large tests do.

Large tests are not run using `tox` and currently reference `http://localhost`.

- Assert Core (Large)
- Assert Core (Medium)

### Linting and code style

Linting and code style can be managed in few different ways. The first place this repo will suggest is in the code editor. It is easiest to manage this when a team agrees to use tools that are easy to configure the same way. For instance everyone agreeing to use Visual Studio Code with the same linting and code style packages. For python, picking something that enforces [Pep8](https://www.python.org/dev/peps/pep-0008/) standards is strongly encouraged.

Since python is complied at runtime the second place to manage linting and consistent code style verification is when tests are ran (see Testing). This repo will execute [pycodestyle](https://pypi.org/project/pycodestyle/), and [codecoverage](https://coverage.readthedocs.io/en/v4.5.x/) as part of tox testing.

### Testing

This repo uses [pytest](https://docs.pytest.org/en/latest/getting-started.html) and [tox](https://tox.readthedocs.io/en/latest/) to facilitate testing. In addition Tox will assert linting, verify code style and executing code coverage reports. Tests are stored in the `/tests/tox_tests` folder. [Fixtures](https://docs.pytest.org/en/latest/fixture.html) are pytest abstractions for a particular type of reusable test code. Fixtures used to support tox tests are stored in `tests/configuration`.

Tests are grouped by "size" as defined by google. Here is an interesting [blog](https://mike-bland.com/2011/11/01/small-medium-large.html) and another [blog](https://testing.googleblog.com/2010/12/test-sizes.html) about test sizes. Medium tests are prefixed with `test_med`. Large tests are prefixed with `test_lrg`.

**_Note: Explicit small tests are not needed in languages like python that compile at runtime. Tox performs them at the time medium tests are ran_**

#### Brief Summary

- small tests: Linting, code style, code compilation checks
- medium tests: Business logic that can run on localhost
- large tests: Assert the connection between components and systems
- x-large tests: Assert the end to end interaction of an entire ecosystem ususally from the perspective of a customer

#### Execution

- Execute the command `tox` from root of the repo directory to assert all tests.
- Execute the command `tox tests/tox_tests/test_med*` from root of the repo directory to assert just medium tests.
- Execute the command `tox tests/tox_tests/test_lrg*` from root of the repo directory to assert just large tests.
- Execute the command `tox tests/tox_tests/[file name]` from root of the repo directory to assert just a single test

#### Code Coverage

This repo uses [codecoverage](https://coverage.readthedocs.io/en/v4.5.x/) to facilitate testing coverage. One Hundred percent code coverage is expected. Each tox execution currently overwrites an HTML coverage report to `tests/codecoverage/index.html`

**Code Coverage Report Exclusions:** We can use the comment `# pragma: no cover` to mark lines that of code that will be reported as excluded.

## Misc configuration files

- .gitignore - a fine start to common things that should be ignored in a python repo
- tox.ini - config file for Tox
- poetry.lock - [poetry's](https://python-poetry.org/docs/basic-usage/#installing-with-poetrylock) locked dependencies and verisons
- pyproject.toml - [poetry's](https://python-poetry.org/docs/basic-usage/#installing-with-poetrylock) dependecy definitions
- .secrets - a path for storing local uncommited singer config files to ensure they are not checked into git repos.

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-harvest-engine
meltano install
```

Add env vars
```
MELTANO_STATE_ID=harvest-engine-target-json
```


Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-harvest-engine --version
# OR run a test `elt` pipeline:
meltano elt tap-harvest-engine target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://gitlab.com/meltano/singer-sdk/-/blob/main/docs/dev_guide.md) for more instructions on how to use the SDK to
develop your own taps and targets.
