from odoo import api, fields, models


class req_timesheet(models.Model):
    _name = "req.timesheet"
    _description = "Tasks done by user during a time"

    user_id = fields.Many2one('res.users', 'User', required=True)
    timeentry_ids = fields.One2many('req.timeentry', 'timesheet_id', string='Task')
    date = fields.Date('Date')
    start = fields.Float('Start')
    end = fields.Float('End', compute='_compute_end', inverse='_compute_duration', store=True)
    duration = fields.Float('Duration', compute='_compute_duration', inverse='_compute_end')
    time_filled = fields.Float('Filled in', compute='_compute_total')
    time_to_fill = fields.Float('To fill', compute='_compute_remaining')

    @api.onchange("start")
    def _onchange_start(self):
        if self.start < 0:
            self.start = 0
        if self.start > 24:
            self.start = 24
        if self.start > self.end:
            self.end = self.start
    
    @api.onchange("end")
    def _onchange_end(self):
        if self.end < 0:
            self.end = 0
        if self.end > 24:
            self.end = 24
        if self.end < self.start:
            self.start = self.end

    @api.depends('start', 'end')
    def _compute_duration(self):
        for record in self:
            if record.end:
                record.duration = record.end - record.start
            else:
                record.duration = 0
    
    @api.depends('duration')
    def _compute_end(self):
        for record in self:
            if record.duration:
                record.end = record.start + record.duration
            else:
                record.end = 0

    @api.depends('timeentry_ids.duration')
    def _compute_total(self):
        for record in self:
            record.time_filled = 0
            for entry in record.timeentry_ids:
                record.time_filled += entry.duration
    
    @api.depends('timeentry_ids', 'duration')
    def _compute_remaining(self):
        for record in self:
            record.time_to_fill = record.duration - record.time_filled