![Python Versions](https://img.shields.io/badge/3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue) ![Style Black](https://warehouse-camo.ingress.cmh1.psfhosted.org/fbfdc7754183ecf079bc71ddeabaf88f6cbc5c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667) [![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)

# 🚪 Introduction Awesome Panel CLI

THIS PROJECT IS IN AN EARLY ALPHA STATE AND WILL CHANGE. USE AT YOUR OWN RISK.

The aim of the `awesome-panel-cli` project is to turn any user of the CLI into a
highly productive developer of high quality Panel apps.

To do this the `awesome-panel-cli` provides an opinionated command line interface (CLI) `pn`.

For example you can create a new app as simple as

```bash
pn create app
```

This project draws inspiration from other CLI tools like

- [Angular CLI](https://angular.io/cli).
- [Django management commands](https://www.djangoproject.com/)
- [React Create App](https://reactjs.org/docs/create-a-new-react-app.html)

But the `awesome-panel-cli` also aims to provide additional, unique features like easy deployment.

## Hacktoberfest

If you are looking to contribute you can find ideas in the [issue tracker](https://github.com/awesome-panel/awesome-panel-cli/issues)).

[![Hacktober Fest](https://github.blog/wp-content/uploads/2022/10/hacktoberfestbanner.jpeg?fit=1200%2C630)](https://github.com/awesome-panel/awesome-panel-cli/issues).

## 🧳 Prerequisites

- A working [Python](https://www.python.org/downloads/) environment.
- [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## 📙 How to

Below we describe how to get started.

## 🚀 Install for usage

You can install the package via

```bash
pip install awesome-panel-cli
```

If you additionally want to serve the *intro* notebook or *example* apps you should run

```bash
pip install awesome-panel-cli[all]
```

You will then have access to a powerful command line interface invoked using the command `pn`.

Try running

```bash
pn --help
```

## 💻 Install for Development

To install for development you need to run

```bash
pip install pip -U
pip install -e .[dev]
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
