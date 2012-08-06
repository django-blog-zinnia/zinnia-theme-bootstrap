======================
Zinnia-theme-bootstrap
======================

Zinnia-theme-bootstrap is a python package providing a theme builded on
`Bootstrap` for `django-blog-zinnia`_.

Installation
============

Once `Zinnia is installed`_ on your Django project and this package installed
on your `PYTHON_PATH`, simply register the `zinnia_bootstrap` application in
the `INSTALLED_APP` section of your project's settings.

Now Zinnia is Bootstrap ready.

.. warning::
   * `zinnia_bootstrap` must be registered before the `zinnia` app to bypass
     the loading of the Zinnia's templates.
   * You need to use the ``django.template.loaders.eggs.Loader`` template
     loader if you have installed the package as an egg.


.. _`Bootstrap`: http://twitter.github.com/bootstrap/
.. _`django-blog-zinnia`: http://www.django-blog-zinnia.com/
.. _`Zinnia is installed`: http://django-blog-zinnia.com/documentation/getting-started/install/

