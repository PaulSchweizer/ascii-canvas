import nox
import os


@nox.session(python=["3.6"])
def static_type(session):
    session.install("mypy")

    session.run("mypy", "--ignore-missing-imports", "ascii_canvas")


@nox.session(python=["2.7", "3.4", "3.5", "3.6"])
def pytests_no_hints(session):
    session.install("-r", "test-requirements.txt")

    session.run("python", "-m", "pytest", "--spec", "-s", os.path.join("tests"))
