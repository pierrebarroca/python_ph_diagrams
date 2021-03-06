#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_ph_diagrams` package."""

import pytest


# from python_ph_diagrams import python_ph_diagrams
from python_ph_diagrams.python_ph_diagrams import PlotProps

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    assert(PlotProps('HEOS', 'R744'))
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
