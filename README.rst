Embedly Extension for Python-Markdown
=====================================

A Python-Markdown extension for embeded url using `Embedly <http://embed.ly/>`_ .

.. code::

  [https://github.com/yymm/mdx_embedly:embed]

becomes

.. code::

  <p>
  <a class="embedly-card" href="https://github.com/yymm">embed.ly</a>
  <script async src="//cdn.embedly.com/widgets/platform.js"charset="UTF-8"></script>
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
