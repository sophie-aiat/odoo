from odoo import fields, models


class req_at(models.Model):
    _name = "req.at"
    _description = "possible ateliers"

    name = fields.Char(required=True)
    product_ids = fields.One2many("req.products", "at_id", string="Products")
