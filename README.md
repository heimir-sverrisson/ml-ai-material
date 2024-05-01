# Installation instructions

## Create and activate the virtual environment for Python

If you're on a Mac, where the default shell is `zsh`, you'll need to run `bash` first, as `venv` is only compatible with `bash`. Once you've done that, continue with the following.

```bash
python3 -m venv venv
source venv/bin/activate
```

This should activate a private version of python 3.11. You can check it with

```bash
which python3
```

That should show the path to `venv/bin/python3`.

## Using the virtual environment

By using an virtual environment you isolate this installation from the python
installation on your machine and stuff you might have installed as a `--user`.

Every time you want to run this code you need to activate it with:

```bash
source venv/bin/activate
```

And when you want to use your regular python setup, just run:

```bash
source venv/bin/deactivate
```

## Install Jupyter Notebook in the virtual environment

```bash
pip3 install jupyterlab
pip3 install notebook
python3 -m ipykernel install --user --name=venv
```

## Install other libraries

```bash
pip3 install psycopg2
pip3 install scikit-learn
pip3 install numpy
pip3 install matplotlib
pip3 install pandas
pip3 install torch
pip3 install torchvision
```

Beware that the `torch` package is several GBytes!

## Install a Dockerized PostgreSQL with a vector extension

```bash
cd postgresql
docker compose up
# `db` service logs will output in this terminal
```

Open another terminal in the project directory and run:

```bash
cd postgresql
./do_load.sh
Password: postgres
...
Password: postgres
```

The script will prompt you twice for the password and just enter `postgres`.

## Prepare the MNIST data set

If you're still in the `postgresql` directory, run `cd ..`. Then:

```bash
tar -xzf MNIST.tgz
```

## Run the Jupyter Notebook samples

```bash
jupyter notebook
```

In the main tab just double-click on any of the `.ipynb` files on the list to open a new tab
with that notebook. A tutorial on Jupyter Notebook can be found at [Jupiter Notebook Tutorial](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html)

## Natural Language Processing

Remember to activate your virtual environment with `source venv/bin/activate` if not already
activated.

```bash
pip3 install spacy
python3 -m spacy download en_core_web_trf
```

The download is about 500 MB. A much smaller model is `en_core_web_sm`.

## Parts of speech

If Jupyter Notebook is not already running, start it again and work on the `SpaCy.ipynb`.

## Decision trees

If you're on Mac and using Homebrew to manage packages, run `brew install graphviz`.

Use `pip3` to install `graphviz` and `scikit-learn-tree` packages into the Python virtual
environment and run `python3 decision_tree.py` to create a decision tree for the `Titanic`
dataset. In the input file `titanic_2.csv` `Sex=1` means `male` and `0` female.

The python script creates `Titanic.pdf`. In the `values` vector, the first element is how
many died and the second how many survived. The graph has `True` condition to the left
and `False` to the right. The root node is a decision on sex, so women are on the left
side (`Sex <= 0.5`) and men on the right.
