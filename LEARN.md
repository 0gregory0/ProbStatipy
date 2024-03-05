# How to Create a Python Package and Publish it on PYPI

These are the steps I followed to create the ProbStatipy package and publish it
on [PyPI](https://pypi.org/). You can use these steps to create your own Python
package and publish it on PyPI. Once your package is on PYPI, anyone can
download it using the famous `pip install <package_name>` command on their
terminal.

---

## Steps
1. Install required modules
2. Create the necessary folders
3. Create a README.md file
4. Create a LICENCE.txt file (or LICENSE.txt if you prefer the American English)
5. Create a pyproject.toml file
6. Build
7. Upload to PyPI

> This tutorial assumes that you already have an account on [pypi](pypi.org) or [test pypi](test.pypi.org) depending on where you want to publish your package. If not, click on one of the hyperlinks, then click on register and sign-up. Ensure to enable 2FA (two-factor authentication). 

---

##  Detailed Steps

### 1. Install Required Modules
First off, ensure you have python3 and pip3 installed. Ensure pip is on its
latest version by running

```bash
py -m pip install --upgrade pip
```

The other modules/packages that you need are:
* setuptools
* wheel
* twine
* build

Run the following commands to install/upgrade them

```bash
py -m pip install --upgrade setuptools
```

```bash
py -m pip install --upgrade twine
```

```bash
py -m pip install --upgrade build
```

```bash
py -m pip install --upgrade wheel
```

### 2. Create the Necessary Folders

Create the necessary folders, ensuring your file structure looks like this:

```
packaging_tutorial/
└── src/
    └── example_package_0gregory0/
        ├── example.py
        └── __init__.py
```

```packaging_tutorial/``` is the root folder. You can name this whatever you
want.

```src/``` is the folder which contains all your source code.

```example_package/``` is where you will store all your modules. For example,
```example.py``` is a module stored in this folder (you can name your module
whatever you want or have more than one module).  For convention and
convenience, the folder should be given the same name that you intend your
package to be called. To ensure your package name is unique, do a name search
on [pypi](pypi.org) or [test pypi](test.pypi.org) depending on where you want
to publish your package.

```__init__.py``` is a special file that is required to be in the same
directory as your modules. Ensure that you include it. It is possible to leave
it out, but that is a more advanced approach that is outside the scope of this
tutorial.

In the case of the ProbStatipy Package, this is how the file structure looks
like:

```
probstatipy_package/
├── src/
│    └── ProbStatipy/
│        ├── central.py
│        ├── probability.py
│        ├── spread.py
│        └── __init__.py
├─── .gitignore
├─── CHANGELOG.md
├─── LEARN.md
├─── LICENSE.txt
├─── pyproject.toml
├─── README.md
└── Requirements.txt
```

However, for now, just concern yourself with the root folder (in my case its
the "probstatipy_package" folder) and the "src" folder. We'll go over the rest
of the files shortly.

### 3. Create a README.md file
A ```README.md``` file is a file where you document your package, so that other
developers can know how your package works. It has a ```.md``` file extension
meaning that it is written in markdown format.
([Learn more about markdown](https://guides.github.com/features/mastering-markdown/)).
We create and place this file in our root folder, `packaging_tutorial`.

### 4. Create a LICENCE.txt file
Also known as `LICENSE.txt`, this file is placed in the root folder
(`packaging_tutorial`). The `LICENCE.txt` is a file that tells developers what
they are and aren't allowed to do with your code. Remember that code is
intellectual property and you can reserve your rights by including a licence.
When you don't include a a licence, your code is automatically given the
exclusive license that only gives you the right to copy and distribute your
code and developers may not contribute to your project for fear of facing a
copyright strike. ([Learn more about licenses](https://choosealicense.com/)).
The most popular licence is the
[MIT Licence](https://choosealicense.com/licenses/mit/) due to its concise
nature. For this tutorial, I chose the
[Apache Licence](https://choosealicense.com/licenses/apache-2.0/).

### 5. Create a pyproject.toml file
We create the `pyproject.toml` in the root folder(`packaging_tutorial`).

This is what bing chat had to say about this file:

...

The **`pyproject.toml`** file is **essential** when creating a Python package
for publishing on PyPI (Python Package Index). Here's why:

1. **Build Backend Configuration**: The `pyproject.toml` specifies the build
backend to use for your project. It tells tools like `pip` and `build` how to
build your package. The `[build-system]` section in this file defines the
backend and its dependencies.

2. **Metadata and Configuration**: The `pyproject.toml` contains crucial
metadata about your package, including:
   - **Name**: The distribution name of your package.
   - **Version**: The package version.
   - **Authors**: Information about the author(s) and maintainer(s).
   - **Description**: A short summary of the package.
   - **Requires-Python**: Supported Python versions.
   - **Classifiers**: Additional metadata (e.g., license, compatibility).

3. **Dependency Management**: The `requires` key lists packages needed to build
your package. Frontends (like `pip`) install these dependencies automatically
during the build process.

4. **Source Distribution**: When you run the build command, the
`pyproject.toml` guides the creation of source distribution archives
(e.g., `.tar.gz`). These archives are uploaded to PyPI and can be installed by
users.

In summary, including the `pyproject.toml` file is **crucial** for proper
package configuration, building, and distribution. Without it, your package
won't be ready for PyPI.

...

From the first point, you can see that this file helps us build our backend.
You can choose from a number of backends such as
[Setuptools](https://setuptools.pypa.io/en/latest/),
[Flit](https://flit.pypa.io/en/latest/), [PDM](https://pdm-project.org/latest/)
and [Hatchling](https://hatch.pypa.io/latest/). In this tutorial, we
use Setuptools.

Add this to the `pyproject.toml` file to configgure `setuptools` as our backend.

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

Now, we add metadata to the same file

```toml
[project]
name = "example_package_0gregory0"
version = "0.0.1"
authors = [
  { name="GREGORY OCHIENG OPONDI", email="ds4gregory@gmail.com" },
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
]

[project.urls]
Homepage = "https://github.com/pypa/sampleproject"
Issues = "https://github.com/pypa/sampleproject/issues"
```

* `name` is the distribution name of your package. This can be any name as long
as it only contains letters, numbers, `.`, `_` , and `-`. It also must not
already be taken on PyPI.
**Be sure to update this with your unique package name for this tutorial**,
as this ensures you won’t try to upload a package with the same name as one
which already exists.

* `version` is the package version. (Some build backends allow it to be
specified another way, such as from a file or Git tag.)

* `authors` is used to identify the author of the package; you specify a name
and an email for each author. You can also list `maintainers` in the same
format.

* `description` is a short, one-sentence summary of the package.

* `readme` is a path to a file containing a detailed description of the package.
This is shown on the package detail page on PyPI. In this case, the description
is loaded from `README.md` (which is a common pattern). There also is a more
advanced table form described in the pyproject.toml guide.

* `requires-python` gives the versions of Python supported by your project. An
installer like pip will look back through older versions of packages until it
finds one that has a matching Python version.

* `classifiers` gives the index and pip some additional metadata about your
package. In this case, the package is only compatible with Python 3, is
licensed under the MIT license, and is OS-independent (That is from the
[online tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/#packaging-python-projects).
I chose the Apache License, but everything else remains the same). You should
always include at least which version(s) of Python your package works on, which
license your package is available under, and which operating systems your
package will work on. For a complete list of classifiers, see
https://pypi.org/classifiers/.

* `urls` lets you list any number of extra links to show on PyPI. Generally this
could be to the source, documentation, issue trackers, etc.

### 6. Build
While some tutorials add the metadata in a `setup.py` file and use the
`setup.py` file to execute commands, I chose not to. This is because running
this file as a script (e.g. python setup.py sdist) is strongly discouraged, and
that the majority of the command line interfaces are (or will be) deprecated. It
is also recommended to expose as much as possible configuration in a more
declarative way via the `pyproject.toml` or `setup.cfg`, and keep the setup.py
minimal with only the dynamic parts (or even omit it completely if applicable).

So I decided to omit it completely and work with `pyproject.toml`

Now that we are solely working on `pyproject.toml`, we can build our package by
running the following command:

```bash
python -m build
```

You now have your distribution ready (e.g. a tar.gz file and a .whl file in the
dist directory), which you can
[upload to PyPI](https://twine.readthedocs.io/en/stable/index.html)!

> Note: If you are tracking all this with git, you may also want to add a `.gitignore` file at this point to ignore the dist folder and the egg-info folder. Ensure the `.gitignore` file is in the root folder and add the following
> ```.gitignore
> # Ignore dist folder in the root
> /dist/
> # Ignore example.egg-info folder inside src
> /src/example_package_0gregory0.egg-info/
> ```

### 7. Upload to PyPI
Finally, it’s time to upload your package to the Python Package Index! Once
again, I assume that you've already created an account and enabled 2FA on
[PyPI](pypi.org) and Test [PyPI](test.pypi.org). Ok, I know I said it's time to
upload our package to PyPI but first...

![Hold up meme: A drawing of a cartoon stretching its hands signaling the viewer to stop with the caption "Wait a minute, Hold Up"](https://th.bing.com/th/id/OIP.UjDCCX5rd_2CFE7gFXxyDwHaFX?w=285&h=206&c=7&r=0&o=5&dpr=1.5&pid=1.7)

Let's first upload to Test PyPI to ensure everything works well.

#### 7.1 Uploading to Test PyPI

To securely upload your project, you’ll need a
[PyPI API token](https://test.pypi.org/manage/account/#api-tokens). Create one,
setting the “Scope” to “Entire account”.
**Don’t close the page until you have copied and saved the token — you won’t see that token again.**
Now, let's use `twine` to upload our package to Test PypI by running the
following command:

```bash
py -m twine upload --repository testpypi dist/*
```

Upon success, you should see an output window similar to this:

```powershell
Uploading example_package_0gregory0-0.0.1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 23.4/23.4 kB • 00:00 • ?
Uploading example_package_0gregory0-0.0.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 22.8/22.8 kB • 00:00 • ?

View at:
https://test.pypi.org/project/example-package-0gregory0/0.0.1/
```

You can test if this worked by
- moving into a new directory (outside your root directory)
- activating a virtual environment
- installing your package using the following command:

```bash
py -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE
```
Output:
```powershell
Collecting example-package-YOUR-USERNAME-HERE
  Downloading https://test-files.pythonhosted.org/packages/.../example_package_YOUR_USERNAME_HERE_0.0.1-py3-none-any.whl
Installing collected packages: example_package_YOUR_USERNAME_HERE
Successfully installed example_package_YOUR_USERNAME_HERE-0.0.1
```
- run python and import the package

```bash
py
```

```bash
>>> from example_package_YOUR_USERNAME_HERE import example
>>> example.add_one(2)
3
```

If everything went well to this point, now you can upload your package to PYPI
with a few points to note

#### 7.2 Uploading to PYPI
When you are ready to upload a real package to the Python Package Index you can
do much the same as you did in this tutorial, but with these important
differences:

* Choose a memorable and unique name for your package. You don’t have to append
your username as you did in the tutorial, but you can’t use an existing name.

* Register an account on [pypi](https://pypi.org) - note that these are two
separate servers and the login details from the test server are not shared with
the main server.

* Use `twine upload dist/*` to upload your package and enter your credentials
for the account you registered on the real PyPI. Now that you’re uploading the
package in production, you don’t need to specify `--repository`; the package
will upload to [pypi](https://pypi.org) by default.

* Install your package from the real PyPI using

```bash
python -m pip install [your-package].
```

This tutorial was obtained from the
[packaging.python.org](https://packaging.python.org/en/latest/tutorials/packaging-projects/#packaging-python-projects) website.