![Python Versions](https://img.shields.io/badge/3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue) ![Style Black](https://warehouse-camo.ingress.cmh1.psfhosted.org/fbfdc7754183ecf079bc71ddeabaf88f6cbc5c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667) [![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)

# 🚪 Introduction Awesome Panel CLI

THIS PROJECT IS IN AN EARLY ALPHA STATE.

The Awesome Panel CLI package provides a command line interface to speed up your workflow when working with Panel.

For example you can create a new app by

```bash
pn create app
```

## 🧳 Prerequisites

- Python
- [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## 📙 Using

You can install the package via

```bash
pip install awesome-panel-cli
```

If you additionally want to serve the *intro** notebook or *hello world* apps you should run

```bash
pip install awesome-panel-cli[all]
`` 

You will then have access to a powerful command line interface invoked using the command `pn`.

```bash
pn --help
```

And get additional help via `--help`

```bash
pn create component --help
```

### 🚗 Creating a new project

Executing:

```bash
pn create project
```

## ‎‍💻 Development

To install for development you need to run

```bash
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