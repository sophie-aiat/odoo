from odoo import api, fields, models
from odoo.exceptions import ValidationError


class req_components(models.Model):
    _name = "req.components"
    _description = "componenets of products"

    name = fields.Char(required=True)
    product_id = fields.Many2one("req.products", string="Belongs to")
