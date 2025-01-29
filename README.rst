FastAPI Blueprint
=================

.. image:: https://badge.fury.io/py/your-package-name.svg
    :target: https://pypi.org/project/fastapi-blueprint/

.. image:: https://static.pepy.tech/badge/fastapi-blueprint
    :target: https://pepy.tech/projects/fastapi-blueprint

FastAPI Blueprint is a command-line tool designed to help developers quickly generate a structured project file system for FastAPI applications. With this tool, you can jumpstart your FastAPI project with a clean, modular, and scalable architecture.

Features
--------

- Automatically generate directories and files for a standard FastAPI project.
- Includes support for:
  - ``routers``
  - ``models``
  - ``schemas``
  - ``services``
  - ``utils``
- Customizable templates to suit your project needs.
- Simple and intuitive CLI commands.

Installation
------------

To install FastAPI Blueprint, use pip:

.. code-block:: bash

    pip install fastapi-blueprint

Usage
-----

Generate a New Project Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run the following command to create a new FastAPI project:

.. code-block:: bash

    fastapi-blueprint init my_project

This will generate the following structure:

.. code-block:: text

    my_project/
    ├── app/
    │   ├── routers/
    │   ├── models/
    │   ├── schemas/
    │   ├── services/
    │   ├── utils/
    │   └── main.py
    └── requirements.txt

Adding Components
^^^^^^^^^^^^^^^^^

You can add individual components like routers or models:

.. code-block:: bash

    fastapi-blueprint add router users

This will create a new router file under the ``routers/`` directory.

Customize Templates
^^^^^^^^^^^^^^^^^^^

FastAPI Blueprint allows you to define your own templates for files and structures. Simply modify the default templates in the ``~/.fastapi-blueprint/templates/`` directory.

Contributing
------------

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch: ``git checkout -b feature-name``
3. Commit your changes: ``git commit -m 'Add feature-name'``
4. Push to the branch: ``git push origin feature-name``
5. Open a pull request.

License
-------

This project is licensed under the MIT License. See the `LICENSE`_ file for more details.

Acknowledgments
---------------

FastAPI Blueprint is inspired by the simplicity and scalability of FastAPI itself. Thanks to the FastAPI community for building such an amazing framework!