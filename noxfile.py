import nox


@nox.session(venv_backend="uv", python=["3.14", "3.13", "3.12", "3.11", "3.10", "3.9"])
def tests(session):
    session.install("-r", "test_requirements.txt", "--reinstall-package", "win32more")
    session.run("pytest", *(session.posargs or ["tests"]))
