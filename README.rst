protoclass - *Prototype-Oriented Programming in Python.*
========================================================
`Prototype-Oriented Programming <https://en.wikipedia.org/wiki/Prototype-based_programming>`_ in Python at the tip of your fingers in a simple, easy-to-use library.

|PyPI-package-version| |PyPI-license| |PyPI-python-versions| |travis-ci| |readthedocs| |PyPI-downloads-month|
 

Installation
------------

``pip install protoclass``

Usage
-----

.. code:: python


   >>> from protoclass import proto

   # We create a basic object and add some functionality
   >>> jane = proto(first="Jane", last="Doe")
   >>> jane.greet = lambda self: print(self)
   >>> jane.greet()  #doctest: +ELLIPSIS
   <proto object at ...>

   # A more user-friendly would be better.
   # We could modify the `greet` function
   # or we could create another object and inherit from it
   >>> person = proto(first="", last="")
   >>> person.__str__ = lambda self: f"{self.first} {self.last}"
   >>> jane = jane.chain(person)

   # and we should get a better message.
   >>> jane.greet()
   Jane Doe

API Reference
-------------

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **proto(\*\*attrs)**                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Makes a new prototype with given attributes.                                                                                                                                     |
| An empty prototype will be made when no attributes are given.                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **proto.chain(self, other, \*others)**                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Makes self copy attributes from another prototype or multiple other prototypes.                                                                                                  |
| Any previous relationship with other parent prototypes will be automatically severed.                                                                                            |
| When parent prototypes share attributes with the same name, the first parent prototype that has that attribute will be provide it, so the order in which they are given matters. |
| Any change made to parent prototypes will be automatically propagated to this prototype.                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **clone(other, \*others)**                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Makes a new prototype by copying attributes from another prototype or multiple other prototypes.                                                                                 |
| When parent prototypes share attributes with the same name, the first parent prototype that has that attribute will be provide it, so the order in which they are given matters. |
| Any change made to parent prototypes will be automatically propagated to this clone.                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For more information on these functions, call ``help`` on the function
you would like to know more of, like this: ``help(proto)``.
You can also read the docs_.

Contributing
------------
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

.. |made-with-python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/
.. |PyPI-downloads-month| image:: https://img.shields.io/pypi/dm/protoclass.svg
   :target: https://pypi.python.org/pypi/protoclass/
.. |PyPI-package-version| image:: https://img.shields.io/pypi/v/protoclass.svg
   :target: https://pypi.python.org/pypi/protoclass/
.. |PyPI-license| image:: https://img.shields.io/pypi/l/protoclass.svg
   :target: https://pypi.python.org/pypi/protoclass/
.. |PyPI-python-versions| image:: https://img.shields.io/pypi/pyversions/protoclass.svg
   :target: https://pypi.python.org/pypi/protoclass/
.. |travis-ci| image:: https://travis-ci.com/jellowfish/protoclass.svg?branch=master
   :target: https://travis-ci.com/jellowfish/protoclass
.. |readthedocs| image:: https://readthedocs.org/projects/protoclass-jf/badge/?version=latest
   :target: http://protoclass-gidona18.readthedocs.io/?badge=latest
.. _docs: https://protoclass-gidona18.readthedocs.io/en/latest/protoclass.html
