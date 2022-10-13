# 🚪 Awesome Panel CLI

![Python Versions](https://img.shields.io/badge/3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
[![codecov](https://codecov.io/gh/awesome-panel/awesome-panel-cli/branch/main/graph/badge.svg?token=MXANQHSUUV)](https://codecov.io/gh/awesome-panel/awesome-panel-cli)
[![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/awesome-panel/awesome-panel-cli/feature/binder)
[![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)

⚠️ THIS PROJECT IS IN AN ALPHA STATE AND WILL CHANGE. USE IT AT YOUR OWN RISK.

We want to

- make it super simple to develop high-quality [Panel](https://awesome-panel.org) data apps.

We provide

- an opinionated command line interface (CLI) `pn` and
- a set of *best practice* templates

You can install and create a new *app* as simple as

```bash
pip install awesome-panel-cli[all]
pn create app
```

![Awesome Panel CLI Intro](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/videos/awesome-panel-cli-intro-small.gif?raw=true)

This project draws inspiration from other CLI tools like
[Angular CLI](https://angular.io/cli),
[Django management commands](https://www.djangoproject.com/),
[django-simple-deploy](https://github.com/ehmatthes/django-simple-deploy) and
[React Create App](https://reactjs.org/docs/create-a-new-react-app.html).

## ⭐ Support

Please support [Panel](https://panel.holoviz.org) and
[awesome-panel](https://awesome-panel.org) by giving the projects a star on Github:

- [holoviz/panel](https://github.com/holoviz/panel).
- [awesome-panel/awesome-panel](https://github.com/awesome-panel/awesome-panel).

Thanks

## ❤️ Contribute

If you are looking to contribute to this project you can find ideas in the [issue tracker](https://github.com/awesome-panel/awesome-panel-cli/issues).

I would love to support and receive your contributions. Thanks.

[![Hacktober Fest](https://github.blog/wp-content/uploads/2022/10/hacktoberfestbanner.jpeg?fit=1200%2C630)](https://github.com/awesome-panel/awesome-panel-cli/issues).

## 🧳 Prerequisites

- A working [Python](https://www.python.org/downloads/) environment.
- [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## 📙 How to

Below we describe how to get started.

### 🚀 Install for usage

You can install the package via

```bash
pip install awesome-panel-cli
```

If you additionally want to serve the *intro* notebook or *example* apps you should run

```bash
pip install awesome-panel-cli[all]
```

You will then have access to a powerful command line interface invoked using the command `pn`.

### ❓ How to figure out which commands are available

Try running

```bash
pn --help
```

![pn help](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/images/pn-help.png?raw=true)

```bash
pn hello --help
```

![pn --help](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/images/pn-hello-help.png?raw=true)

```bash
pn create --help
```

![pn create --help](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/images/pn-create-help.png?raw=true)

```bash
pn create app --help
```

![pn create app --help](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/images/pn-create-app-help.png?raw=true)

```bash
pn create project --help
```

![pn create project --help](https://github.com/awesome-panel/awesome-panel-cli/blob/main/assets/images/pn-create-project-help.png?raw=true)

### 💻 Install for Development

To install for development you will need a fresh and activated virtual environment.

Then run

```bash
git clone https://github.com/awesome-panel/awesome-panel-cli.git
cd awesome-panel-cli
pip install pip -U
pip install -e .[all]
```

Then you can see the available commands via

```bash
pn --help
```

You can run all tests via

```bash
pn test all
```

Please run this command before you `git push` and fix any failing tests.

### 🔥 Install the current `master` branch

If you want to try out or test the newest features you can install the current `master` branch via

```bash
pip install pip -U
pip install git+https://github.com/awesome-panel/awesome-panel-cli.git
```
