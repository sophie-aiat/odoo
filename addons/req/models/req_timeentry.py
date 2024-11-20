from odoo import api, fields, models


class req_timeentry(models.Model):
    _name = "req.timeentry"
    _description = "Time spend by a worker on a task"

    timesheet_id = fields.Many2one('req.timesheet', required=True, ondelete='cascade')
    at_id = fields.Many2one("req.at", string="Atelier", required=True)
    at_product_ids = fields.One2many("req.product", compute="_compute_product_ids")
    product_id = fields.Many2one("req.product", string="Product", domain="[('id', 'in', at_product_ids)]")
    product_component_ids = fields.One2many("req.component", compute="_compute_component_ids")
    component_id = fields.Many2one("req.component", string="Component", domain="[('id', 'in', product_component_ids)]")
    task = fields.Char(string='Description', compute="_compute_task_description")
    duration = fields.Float('Duration')

    @api.depends('at_id', 'product_id', 'component_id')
    def _compute_task_description(self):
        for record in self:
            record.task = record.at_id.name
            if record.product_id:
                record.task += ' : ' + record.product_id.name
                if record.component_id:
                    record.task += ' - ' + record.component_id.name

    @api.onchange("at_id")
    def _onchange_at_id(self):
        self.product_id = False
        self.component_id = False

    @api.onchange("product_id")
    def _onchange_product_id(self):
        self.component_id = False
    
    @api.onchange("component_id")
    def _onchange_component_id(self):
        pass
    
    @api.depends('at_id')
    def _compute_product_ids(self):
        for record in self:
            if record.at_id and len(record.at_id.product_ids) > 0:
                record.at_product_ids = record.at_id.product_ids
            else:
                record.at_product_ids = False
    
    @api.depends('product_id')
    def _compute_component_ids(self):
        for record in self:
            if record.at_id and len(record.product_id.component_ids) > 0:
                record.product_component_ids = record.product_id.component_ids
            else:
                record.product_component_ids = False
