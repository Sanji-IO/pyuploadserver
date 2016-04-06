from setuptools import setup, find_packages

setup(
    name="pyuploadserver",
    version="1.0.0",
    description="A simple upload server.",
    url="https://github.com/Sanji-IO/pyuploadserver",
    author="Sanji Team",
    author_email="sanji@moxa.com",
    packages=find_packages(exclude=['tests*']),
    license="MIT",
    install_requires=["flask"],
    entry_points={
        "console_scripts": [
            "pyuploadserver = pyuploadserver.app:run_server",
        ]
    }
)
