# Mr. Jig

🤖💬

## Setup


### Virtual Environment

It is recommended to develop inside a Python virtual environment. To set one at
see the [[venv
documentation]](https://docs.python.org/3/library/venv.html#how-venvs-work).
Here is a quickstart for Linux.

```shell
# Install environment in venv directory within this repository.
python3 -m venv ./venv

# Active the environment. This is required for each fresh scripting session.
source venv/bin/activate
```

### Dependencies

```shell
# To install dependencies.
pip install -r requirements.txt

# To update the current dependencies list.
pip freeze >requirements.txt
```