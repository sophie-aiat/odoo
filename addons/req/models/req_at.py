from odoo import api, fields, models


class req_at(models.Model):
    _name = "req.at"
    _description = "possible ateliers"

    name = fields.Char(required=True)
    product_ids = fields.One2many("req.product", "at_id", string="Product IDs")
    product_string = fields.Char("Products", compute='_compute_product_string')

    @api.depends('product_ids')
    def _compute_product_string(self):
        for record in self:
            if record.product_ids:
                record.product_string = ""
                i = 0
                while i < 2 and i < len(record.product_ids):
                    record.product_string += record.product_ids[i].name + ', '
                    i += 1
                if i == len(record.product_ids):
                    record.product_string = record.product_string[:-2]
                else:
                    record.product_string += '...'
            else:
                record.product_string = "No products"

    @api.onchange('product_ids')
    def _onchang_product_ids(self):
        pass
