# ✨ Awesome Panel CLI

We want to

- make it super simple to develop high-quality [Panel](https://awesome-panel.org) data apps.

We provide

- an opinionated command line interface (CLI) `pn` and
- a set of *best practice* templates

![Awesome Panel CLI Intro](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/videos/awesome-panel-cli-intro-small.gif?raw=true)

This project draws inspiration from other CLI tools like
[Angular CLI](https://angular.io/cli),
[Django management commands](https://www.djangoproject.com/),
[django-simple-deploy](https://github.com/ehmatthes/django-simple-deploy) and
[React Create App](https://reactjs.org/docs/create-a-new-react-app.html).

⚠️ THIS PROJECT IS IN AN ALPHA STATE AND WILL CHANGE. USE IT AT YOUR OWN RISK.

## 🖥️ Monitor

[![PyPI version](https://badge.fury.io/py/awesome-panel-cli.svg)](https://pypi.org/project/awesome-panel-cli/)
[![Downloads](https://pepy.tech/badge/awesome-panel-cli/month)](https://pepy.tech/project/awesome-panel-cli)
![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
![Test Results](https://github.com/awesome-panel/awesome-panel-cli/actions/workflows/tests.yaml/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/awesome-panel/awesome-panel-cli/branch/main/graph/badge.svg?token=MXANQHSUUV)](https://codecov.io/gh/awesome-panel/awesome-panel-cli)
[![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/MIT)

[![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)
[![Follow on LinkedIn](https://img.shields.io/badge/linked-in-blue)](https://www.linkedin.com/in/marcskovmadsen)

## ⭐ Support

Please support [Panel](https://panel.holoviz.org) and
[awesome-panel](https://awesome-panel.org) by giving the projects a star on Github:

- [holoviz/panel](https://github.com/holoviz/panel).
- [awesome-panel/awesome-panel](https://github.com/awesome-panel/awesome-panel).

Thanks

## ❤️ Contribute

If you are looking to contribute to this project you can find ideas in the [issue tracker](https://github.com/awesome-panel/awesome-panel-cli/issues). To get started check out the [DEVELOPER_GUIDE](DEVELOPER_GUIDE.md).

I would love to support and receive your contributions. Thanks.

[![Hacktober Fest](https://github.blog/wp-content/uploads/2022/10/hacktoberfestbanner.jpeg?fit=1200%2C630)](https://github.com/awesome-panel/awesome-panel-cli/issues).

## 📙 How to

### 🚀 Get started in under a minute

Install the CLI.

```bash
pip install awesome-panel-cli[all]
```

Serve the examples

```bash
pn hello
```

![pn hello](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/videos/pn-hello.gif?raw=true)

### 📒 Get started on Binder

Click the button

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/awesome-panel/awesome-panel-cli/feature/binder)

### ❓ Check out the CLI commands

Try running the commands below

```bash
pn --help
```

![pn help](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/images/pn-help.png?raw=true)

```bash
pn create --help
```

![pn create --help](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/images/pn-create-help.png?raw=true)

```bash
pn create app --help
```

![pn create app --help](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/images/pn-create-app-help.png?raw=true)

### 🎁 Create an app

Run

```bash
pn create app streaming_indicators
```

Serve

```bash
panel serve streaming_indicators.py
```

![Streaming Indicators](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/videos/streaming_indicators.gif?raw=true)

### 🔥 Install the current `master` branch

If you want to try out or test the newest features you can install the current `master` branch via

```bash
pip install pip -U
pip install git+https://github.com/awesome-panel/awesome-panel-cli.git
```
