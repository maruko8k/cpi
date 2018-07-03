#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python objects for modeling Consumer Price Index (CPI) data structures.
"""


class ObjectList(list):
    """
    A custom list that allows for lookups by the "id" attribute of objects.
    """
    def get(self, key):
        try:
            return (obj for obj in self if obj.id == key).next()
        except StopIteration:
            raise KeyError("Object with id {} could not be found".format(key))


class Area(object):
    """
    A geographical area where prices are gathered monthly.
    """
    def __init__(self, code, name):
        self.id = code
        self.code = code
        self.name = name

    def __repr__(self):
        return "<Area: {}>".format(self.__str__())

    def __str__(self):
        return self.name


class Item(object):
    """
    A consumer item that has its price tracked.
    """
    def __init__(self, code, name):
        self.id = code
        self.code = code
        self.name = name

    def __repr__(self):
        return "<Item: {}>".format(self.__str__())

    def __str__(self):
        return self.name


class Period(object):
    """
    A time period tracked by the CPI.
    """
    def __init__(self, code, abbreviation, name):
        self.id = code
        self.code = code
        self.abbreviation = abbreviation
        self.name = name

    def __repr__(self):
        return "<Period: {}>".format(self.__str__())

    def __str__(self):
        return self.name

    @property
    def month(self):
        """
        Returns the month integer for the period.
        """
        if self.id in ["M13", "S01", "S03"]:
            return 1
        elif self.id == "S02":
            return 7
        else:
            return int(self.id.replace("M", ""))


class Periodicity(object):
    """
    A time interval tracked by the CPI.
    """
    def __init__(self, code, name):
        self.id = code
        self.code = code
        self.name = name

    def __repr__(self):
        return "<Periodicity: {}>".format(self.__str__())

    def __str__(self):
        return self.name


class Series(object):
    """
    A set of CPI data observed over an extended period of time over consistent time intervals ranging from
    a specific consumer item in a specific geographical area whose price is gathered monthly to a category
    of worker in a specific industry whose employment rate is being recorded monthly, etc.

    Yes, that's the offical government definition. I'm not kidding.
    """
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "<Series: {}>".format(self.__str__())

    def __str__(self):
        return self.id

    @property
    def survey_code(self):
        return self.id[:2]

    @property
    def seasonal_code(self):
        return self.id[2:3]

    @property
    def periodicity_code(self):
        return self.id[3:4]

    @property
    def area_code(self):
        return self.id[4:8]

    @property
    def item_code(self):
        return self.id[8:]


class Index(object):
    """
    A Consumer Price Index value generated by the Bureau of Labor Statistics.
    """
    def __init__(self, series, date, year, period_type, value):
        self.series = series
        self.date = date
        self.year = year
        self.period_type = period_type
        self.value = value

    def __repr__(self):
        return "<Index: {}>".format(self.__str__())

    def __str__(self):
        return "{} ({}): {}".format(self.date, self.period_type, self.value)
