# This file is part of the stock_measurements_shape module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockMeasurementsShapeTestCase(ModuleTestCase):
    'Test Stock Measurements Shape module'
    module = 'stock_measurements_shape'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockMeasurementsShapeTestCase))
    return suite