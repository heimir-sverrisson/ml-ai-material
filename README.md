# Installation instructions

## Create and activate the virtual environment for Python

```bash
python -m venv venv
source venv/bin/activate
```

This should activate a private version of python 3.11. You can check it with

```bash
which python
```

That should show the path to `venv/bin/python`.


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
pip install jupyterlab
pip install notebook
python -m ipykernel install --user --name=venv
```

## Install other libraries

```bash
pip install psycopg2
pip install scikit-learn
pip install numpy
pip install matplotlib
pip install pandas
pip install torch
pip install torchvision
```

Beware that the `torch` package is several GBytes!

## Install a Dockerized PostgreSQL with a vector extension

```bash
cd postgresql
docker-compose start
./do_load.sh
Password: postgres
...
Password: postgres
```

The script will prompt you twice for the password and just enter `postgres`.

## Prepare the MNIST data set

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

Remember to activate your virtual environment with `source venv/bin/deactivate` if not already
activated.

```bash
pip install spacy
python -m spacy download en_core_web_trf
```

The download is about 500 MB. A much smaller model is `en_core_web_sm`.

## Parts of speech

If Jupyter Notebook is not already running, start it again and work on the `SpaCy.ipynb`.
