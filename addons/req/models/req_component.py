from odoo import api, fields, models
from odoo.exceptions import ValidationError


class req_component(models.Model):
    _name = "req.component"
    _description = "componenets of products"

    name = fields.Char(required=True)
    product_id = fields.Many2one("req.product", string="Belongs to", required=True, ondelete='cascade')
