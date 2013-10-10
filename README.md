Club Finances Site
==================

A Django based generic website for generating site for keeping track of a club's
finances. This was inspired by 

Prerequisites
-------------

Python 2.7 (Unfortunately `dj-static` does not yet support Python 3)
Pip
Virtualenv (Highly recommended though not strictly necessary)
And an internet connection (Which you presumably already have)

Installation and Setup
----------------------

After cloning this repository via `git clone`, run `pip install -r
requirements.txt` and then go to

    club_finances/club_finances/settings/sensitive.py

and change all the values there to whatever values you need. Note that if you
have a project with publicly available source code, it is best to _not_ include
this file with the rest of source code so that users do not have the ability to
view things like passwords and user-names.

How to Use
----------

The way that the site works is that after a login page, users get to see a list
of the most recent financial transactions that have been carried out. Normal
users cannot modify these financial transactions; that can only be done be done
via the admin page which only site administrators have access to.

Currently the site is fairly bare bones. Django's default admin page takes care
of the administrative duties of creating new users, assigning them privileges,
and changing financial transactions.

Features
--------

Ability to import CSV files to make new financial transaction
