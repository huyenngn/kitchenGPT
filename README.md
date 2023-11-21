# kitchenGPT

![image](https://github.com/huyenngn/kitchengpt/actions/workflows/build-test-publish.yml/badge.svg)
![image](https://github.com/huyenngn/kitchengpt/actions/workflows/lint.yml/badge.svg)

Backend for smart fridge and smart oven operations at ZEKI [available on Docker Hub](https://hub.docker.com/r/huyenngn/kitchengpt).

# Documentation

Read the [full documentation on Github pages](https://huyenngn.github.io/kitchengpt).

# Usage

Create a .env file:

```
OPENAI_API_KEY=<youropenaikey>
```

From the project's root directory, run:

```
docker-compose -f deploy/docker-compose.yml up -d --build
```

To stop, run:

```
docker-compose -f deploy/docker-compose.yml down -v
```

# Installation

To set up a development environment, clone the project and install it into a
virtual environment.

```sh
git clone https://github.com/huyenngn/kitchengpt
cd kitchengpt
python -m venv .venv

source .venv/bin/activate.sh  # for Linux / Mac
.venv\Scripts\activate  # for Windows

pip install -U pip pre-commit
pip install -e '.[dev,test]'
pre-commit install
```

# Contributing

We'd love to see your bug reports and improvement suggestions! Please take a
look at our [guidelines for contributors](CONTRIBUTING.md) for details.

# Licenses

Licensed under Apache 2.0 (see full text in
[LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt))

Dot-files are licensed under CC0-1.0 (see full text in
[LICENSES/CC0-1.0.txt](LICENSES/CC0-1.0.txt))
