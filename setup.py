import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open("telegrampy/conf.py").read(), re.M).group(1)

setup(
    name="telegrampy",
    version=version,
    description="Python client to send notifications through Telegram.",
    url="https://github.com/pasqualguerrero/telegrampy",
    author="Pasqual Guerrero",
    author_email="pasqual.guerrero@gmail.com",
    license="MIT",
    packages=["telegrampy"],
    install_requires=[
        "requests>=2.9.0, <=2.18.1",
    ],
    zip_safe=False,
    test_suite="nose.collector",
    tests_require=["nose==1.3.7"],
)
