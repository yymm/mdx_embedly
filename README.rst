=====================================
Embedly Extension for Python-Markdown
=====================================

.. image:: https://travis-ci.org/yymm/mdx_embedly.svg?branch=master
  :target: https://travis-ci.org/yymm/mdx_embedly

.. image:: https://coveralls.io/repos/yymm/mdx_embedly/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/yymm/mdx_embedly?branch=master

.. image:: https://img.shields.io/pypi/v/mdx_embedly.svg
  :target: https://pypi.python.org/pypi/mdx_embedly

.. image:: https://img.shields.io/pypi/pyversions/mdx_embedly.svg
  :target: https://pypi.python.org/pypi/mdx_embedly

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
  :target: https://opensource.org/licenses/MIT

A Python-Markdown extension for embeded url using `Embedly <http://embed.ly/>`_ .

.. code::

  [https://github.com/yymm/mdx_embedly:embed]

becomes

.. code::

  <p>
  <a class="embedly-card" href="https://github.com/yymm">embed.ly</a>
  <script async src="//cdn.embedly.com/widgets/platform.js" charset="UTF-8"></script>
  </p>

Installation
------------

.. code::

  $ pip install mdx_embedly

Usage
-----

.. code:: python

  import markdown
  # "source"
  html = markdown.markdown(source, extensions=['embedly'])

Usage for Pelican
-----------------

.. code:: python

  MD_EXTENSIONS = ['embedly']

In pelicanconf.py.
