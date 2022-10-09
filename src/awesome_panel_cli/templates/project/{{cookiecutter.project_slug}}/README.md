# 🚪 Introduction {{ cookiecutter.project_slug }}

This purpose of this project ...

## 📙 How to

Below we describe how to get the package or repository installed.

### 🚀 Install for usage

You can install the package via

```bash
pip install {{ cookiecutter.project_slug }}
```

### 💻 Install for development

To install for development you need to

```bash
git clone https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}.git
```

then run

```bash
pip install -e .[dev]
```

Then you can see the available commands via

```bash
pn --help
```

You can run all tests via

```bash
pn test.all
```

Please run this command before you git push.
