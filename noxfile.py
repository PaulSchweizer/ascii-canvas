import nox
import os


@nox.session(python=["3.6", "3.7"])
def static_type(session):
    session.install("mypy")

    session.run("mypy", "--ignore-missing-imports", "ascii_canvas")


@nox.session(python=["3.6", "3.7"])
def pytests_with_hints(session):
    session.install("-r", "test-requirements.txt")

    session.run("python", "-m", "pytest", "--spec", "-s", os.path.join("tests"))


@nox.session(python=["2.7", "3.4", "3.5"])
def pytests_no_hints(session):
    session.install("-r", "test-requirements.txt")

    session.run("cp", "-a", "ascii_canvas", ".ascii_canvas_tmp", external=True)

    session.run("python", "strip-type-hints.py")
    session.run("python", "-m", "pytest", "--spec", "-s", os.path.join("tests"))

    session.run("rm", "-rf", "ascii_canvas", external=True)
    session.run("cp", "-a", ".ascii_canvas_tmp", "ascii_canvas", external=True)
    session.run("rm", "-rf", ".ascii_canvas_tmp", external=True)

