import nox
import os


@nox.session(python="3.6")
def static_type(session):
    session.install('mypy')

    session.run('mypy', '--ignore-missing-imports', 'ascii_canvas')


@nox.session(python="3.6")
def pytests(session):
    session.install('-r', 'test-requirements.txt')

    session.run(
        'python',
        '-m'
        'pytest',
        '--spec',
        '-s',
        os.path.join('tests')
    )


