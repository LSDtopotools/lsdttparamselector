#!/usr/bin/env python

"""Tests for `lsdttparamselector` package."""

import pytest


from lsdttparamselector import lsdttparamselector as lsdps


@pytest.fixture
def test_initiate():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    param = lsdps.lsdttdm()




