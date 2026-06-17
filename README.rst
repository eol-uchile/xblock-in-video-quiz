In Video Quiz XBlock
====================

This XBlock allows for edX components to be displayed to users inside of videos at specific time points.

.. note:: This fork is based in the `Stanford Online xblock-in-video-quiz version 0.1.17, commit 93624bd04a4b613ae53794fd97333192a606aaa8 <https://github.com/Stanford-Online/xblock-in-video-quiz/commit/93624bd04a4b613ae53794fd97333192a606aaa8>`

Installation
------------

Install the requirements into the python virtual environment of your
``edx-platform`` installation by running the following command from the
root folder:

.. code:: bash

    $ pip install -r requirements.txt

Enabling in Studio
------------------

You can enable the In Video Quiz XBlock in Studio through the
advanced settings.

1. From the main page of a specific course, navigate to
   ``Settings ->    Advanced Settings`` from the top menu.
2. Check for the ``advanced_modules`` policy key, and add
   ``"invideoquiz"`` to the policy value list.
3. Click the "Save changes" button.

Package Requirements
--------------------

setup.py contains a list of package dependencies which are required for this XBlock package.
This list is what is used to resolve dependencies when an upstream project is consuming
this XBlock package. requirements.txt is used to install the same dependencies when running
the tests for this package.

License
-------

The In Video Quiz XBlock is available under the AGPL Version 3.0 License.
