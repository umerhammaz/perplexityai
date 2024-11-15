from setuptools import setup, find_packages

setup(
name="perplexityai",
version="0.1",
description="A python api to use perplexity.ai",
long_description=long_description,
long_description_content_type="text/markdown",
url="https://github.com/nathanrchn/perplexityai",
packages=find_packages(),
install_requires=["requests", "websocket-client"]
)
