import nox

@nox.session
def build(session: nox.Session):
    """
    Build the Ansible community website.
    """
    session.install(
      "-r", "requirements.in",
      "-c", "requirements.txt",
    )
    session.run("nikola",
        "build",
        "--strict",
        *session.posargs,
        )

@nox.session
def clean(session: nox.Session):
    """
    Clean the output directory and nikola cache.
    """
    session.install(
      "-r", "requirements.in",
      "-c", "requirements.txt",
    )
    session.run("nikola",
        "clean",
        "--clean-dep",
        *session.posargs,
        )

@nox.session
def serve(session: nox.Session):
    """
    Serve the website from a local browser.
    """
    session.install(
      "-r", "requirements.in",
      "-c", "requirements.txt",
    )
    session.run("nikola",
        "serve",
        "-b",
        *session.posargs,
        )

@nox.session
def spelling(session: nox.Session):
    """
    Spell check the website and blog
    """
    session.install("codespell")
    session.run("codespell",
        *session.posargs,
        "./",
        )

@nox.session
def lint(session: nox.Session):
    """
    Check the website templates for issues.
    """
    session.install("djlint")
    session.run("djlint",
        "-",
        "--lint",
        *session.posargs,
        )

@nox.session
def format(session: nox.Session):
    """
    Format the website templates.
    """
    session.install("djlint")
    session.run("djlint",
        "-",
        "--reformat",
        *session.posargs,
        )
