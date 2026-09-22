````markdown
# ConcoursPrep

ConcoursPrep is a Moroccan public-concours discovery and alert application.

The project is being built progressively to help users discover public concours, compare concours requirements with their profile, and receive relevant alerts.

The initial public source will be `emploi-public.ma`.

## Current state

ConcoursPrep is currently in the foundation stage.

Implemented so far:

- Python project using a `src/` package layout
- isolated `.venv` development environment
- editable package installation
- `concoursprep-health` command
- Git repository with ignored local/generated files

Scraping, persistence, profile matching, notifications, and the API are not implemented yet.

## Prerequisites

- Python 3.11 or newer
- A Unix-like shell such as Bash

Check your Python version with:

```bash
python3 --version
````

## Setup

From the project root, create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install ConcoursPrep in editable mode:

```bash
python -m pip install -e .
```

## Run

Run the health check:

```bash
concoursprep-health
```

Current expected output:

```text
ConcoursPrep health: OK- dev
```

A successful health command should exit with status code `0`.

You can inspect the exit code immediately after running the command with:

```bash
echo $?
```

Expected result:

```text
0
```

## Tests

Automated tests have not been added yet.

The `tests/` directory currently exists as part of the project structure, but the repository does not yet contain a real automated test suite.

Testing commands will be documented here when tests are implemented.

## V0.1 scope

ConcoursPrep V0.1 is intended to progressively support:

* fetching public concours from `emploi-public.ma`
* extracting structured concours metadata
* detecting newly published concours
* detecting meaningfully updated concours
* storing concours records
* storing basic user degree/profile information
* storing user specialty information
* matching degree and specialty against concours requirements
* optionally considering location in profile relevance
* explaining why a concours matched a profile
* sending notifications for relevant new concours
* showing basic concours information
* linking users to the official concours announcement

## Limitations

ConcoursPrep is still under development and most V0.1 capabilities listed above are not implemented yet.

Profile matching will represent **profile relevance**, not definitive legal eligibility.

A ConcoursPrep match must never be interpreted as a guarantee that a user is eligible to apply.

The official concours announcement remains the authoritative source for requirements, deadlines, documents, and eligibility conditions.

```
```
