from odoo import api,fields, models


class req_product(models.Model):
    _name = "req.product"
    _description = "All products Jomy makes"

    name = fields.Char(required=True)
    at_id = fields.Many2one("req.at", string="Atelier", required=True, ondelete='cascade')
    component_ids = fields.One2many("req.component", "product_id", string="Component IDs")
    component_string = fields.Char("Components", compute='_compute_component_string')

    @api.depends('component_ids')
    def _compute_component_string(self):
        for record in self:
            if record.component_ids:
                record.component_string = ""
                i = 0
                while i < 2 and i < len(record.component_ids):
                    record.component_string += record.component_ids[i].name + ', '
                    i += 1
                if i == len(record.component_ids):
                    record.component_string = record.component_string[:-2]
                else:
                    record.component_string += '...'
            else:
                record.component_string = "No components"

    @api.onchange('component_ids')
    def _onchang_component_ids(self):
        pass
