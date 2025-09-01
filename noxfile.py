import nox


@nox.session(
    venv_backend="uv",
    python=[
        "3.14",
        "3.13",
        "3.12",
        "3.11",
        "3.10",
        "3.9",
        "cpython-3.14-windows-x86",
        "cpython-3.13-windows-x86",
        "cpython-3.12-windows-x86",
        "cpython-3.11-windows-x86",
        "cpython-3.10-windows-x86",
        "cpython-3.9-windows-x86",
    ],
)
def tests(session):
    session.install(".")
    session.install("pytest")
    session.run("pytest", *(session.posargs or ["tests"]))
