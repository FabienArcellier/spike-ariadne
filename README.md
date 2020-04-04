## implement a graphql service with ariadne

[![Build Status](https://travis-ci.org/FabienArcellier/blueprint-cli-multicommands-python.svg?branch=master)](https://travis-ci.org/FabienArcellier/blueprint-cli-multicommands-python)

* [ariadne](https://ariadnegraphql.org/)

## Getting started

### 1. Usage : use internal webserver of ariadne

1.1) load the virtual environment

```bash
make install_requirement
make activate
```

1.2) run the webserver

```bash
python -m ariadne_spike.cli webapp
```

1.3) run the graphql query

```bash
curl 'http://127.0.0.1:8000/' -H 'content-type: application/json' --data-binary '{"query":"{\n  user(name: \"fabien\") {name,age}}"}'
```

1.4) use the Graphiql IHM

```bash
localhost:8000
```

### 3. Documentation: the documentation of api is available in UI

* the documentation of the API is available in the UI

### 4. Testability: check the validity of graphql schema

* `gql` instruction allow to check the validity of graphql schema (see [test_query.py](ariadne_spike_tests/acceptances/test_query.py))

### 4. Testability: ensure non regression through acceptance testing

* acceptance test can be running with ``graphql_sync``. This part is missing in official documentation, you have to take a look on [the repository](https://github.com/mirumee/ariadne/blob/master/tests/test_graphql.py)
* acceptance test with mock ?

    Solution 1 : define solver as class

    The dependency injection may be solved with this pattern when necessary. It's useful to ensure
    non regression API on the ``Mutation`` by injecting mock instead of real backend.
    
    ```python
    class UserResolver:
      def __call__(self, obj: Any, info: GraphQLResolveInfo, name=None, age=None):
        return User(name, age)

    user_resolver = UserResolver() # dependency injection go there
    query.create_register_resolver('user')(user_resolver)
    ```
    
    Solution 2 : use stateful module as ``resolver`` collection
    
### 5. Performance : Scalability

### 6. Subscription

Subscription are supported.

I am not confident with the [example given in the documentation](https://ariadnegraphql.org/docs/0.4.0/subscriptions). It suppose the user
has session stickiness on the server.

## The latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/blueprint-cli-multicommands-python.git
```

## Usage

You can run the application with the following command

```bash
python -m mycommand.cli command1 --name fabien

# inside a virtualenv or after installation with pip
mycommand command1 --name fabien
```

## Developper guideline

### Add a dependency

Write the dependency in ``setup.py``. As it's the distribution standard for pypi,
I prefer to keep ``setup.py`` as single source of truth.

I encourage avoiding using instruction as ``pipenv install requests`` to register
a new library. You would have to write your dependency in both ``setup.py`` and ``Pipfile``.

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
make install_requirements_dev
```

### Update release dependencies

Use make to instanciate a python virtual environment in ./venv and freeze
dependencies version on requirement.txt.

```bash
make update_requirements
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
make venv
source venv/bin/activate
```

### Run the linter and the unit tests

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
make lint
make tests
```

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
