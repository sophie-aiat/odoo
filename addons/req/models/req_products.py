from odoo import fields, models


class req_products(models.Model):
    _name = "req.products"
    _description = "All products Jomy makes"

    name = fields.Char(required=True)
    at_id = fields.Many2one("req.at", string="Atelier")
    component_ids = fields.One2many("req.components", "product_id", string="Components")
