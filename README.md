# Djangae Test App

This is a Django project for the purposes of testing [Djangae](https://github.com/lukebpotato/djangae/).

It pulls in a whole load of the Django core tests (tests for Django itself).  Running these tests is highly useful for developing/testing the Datastore Database connector in Djangae.

## Usage

```
$ git submodule update --init
$ python2.7 manage.py test
```
