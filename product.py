# This file is part stock_measurements_shape module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.wizard import Wizard
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['ProductMeasurementsShapeCreation']
__metaclass__ = PoolMeta

MODELS = ['stock.move', 'sale.line', 'purchase.line', 'production.bom.input',
    'production.bom.output']


class ProductMeasurementsShapeCreation(Wizard):
    __name__ = 'product.measurements_shape_creation'

    @classmethod
    def __setup__(cls):
        super(ProductMeasurementsShapeCreation, cls).__setup__()
        cls._error_messages.update({
                'stock_move_readonly':
                ('The stock move is not in draft state.'),
                'sale_readonly': ('The sale is not in draft state.'),
                'purchase_readonly': ('The purchase is not in draft state.'),
                })

    def default_start(self, fields):
        pool = Pool()
        Move = pool.get('stock.move')
        SaleLine = pool.get('sale.line')
        PurchaseLine = pool.get('purchase.line')
        BOMInput = pool.get('production.bom.input')
        BOMOutput = pool.get('production.bom.output')

        context = Transaction().context
        if context['active_model'] in MODELS:
            if context['active_model'] == 'stock.move':
                line = Move(context['active_id'])
                if line.state != 'draft':
                    self.raise_user_error('stock_move_readonly')
            elif context['active_model'] == 'sale.line':
                line = SaleLine(context['active_id'])
                if line.sale.state != 'draft':
                    self.raise_user_error('sale_readonly')
            elif context['active_model'] == 'purchase.line':
                line = PurchaseLine(context['active_id'])
                if line.purchase.state != 'draft':
                    self.raise_user_error('purchase_readonly')
            elif context['active_model'] == 'production.bom.input':
                line = BOMInput(context['active_id'])
            elif context['active_model'] == 'production.bom.output':
                line = BOMOutput(context['active_id'])
            product_id = line.product.id
            new_context = {
                'active_model': 'product.product',
                'active_id': product_id,
                'active_ids': [product_id],
                }
            with Transaction().set_context(new_context):
                return super(ProductMeasurementsShapeCreation,
                    self).default_start(fields)
        return super(ProductMeasurementsShapeCreation,
            self).default_start(fields)

    def do_create_(self, action):
        pool = Pool()
        Move = pool.get('stock.move')
        SaleLine = pool.get('sale.line')
        PurchaseLine = pool.get('purchase.line')
        BOMInput = pool.get('production.bom.input')
        BOMOutput = pool.get('production.bom.output')

        context = Transaction().context
        if context['active_model'] in MODELS:
            if context['active_model'] == 'stock.move':
                line = Move(context['active_id'])
            elif context['active_model'] == 'sale.line':
                line = SaleLine(context['active_id'])
            elif context['active_model'] == 'purchase.line':
                line = PurchaseLine(context['active_id'])
            elif context['active_model'] == 'production.bom.input':
                line = BOMInput(context['active_id'])
            elif context['active_model'] == 'production.bom.output':
                line = BOMOutput(context['active_id'])
            template = line.product.template
            new_template = self.create_find(template)
            line.product = new_template.products[0]
            line.save()
            return None, {}

        return super(ProductMeasurementsShapeCreation, self).do_create_(action)
