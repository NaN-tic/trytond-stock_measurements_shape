# This file is part stock_measurements_shape module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .product import *


def register():
    Pool.register(
        ProductMeasurementsShapeCreation,
        module='stock_measurements_shape', type_='wizard')
