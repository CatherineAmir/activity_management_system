from odoo import fields, models, api

from datetime import datetime,timedelta
UTC_HOURS=3
class Activity(models.Model):
    _name = 'activity.slot'
    _description = 'Activity Slots For Reservation'

    slot_configuration_id = fields.Many2one('',required=True)
    name = fields.Char(compute='_compute_name', string='Name',store=True)
    start_datetime = fields.Datetime(required=True)
    end_datetime = fields.Datetime(required=True)
    max_number = fields.Integer(related='slot_configuration_id.max_number', store=True)
    booked = fields.Boolean()

    reservation_ids=fields.One2many('activity.slot.reservation', 'slot_id')
    @api.depends('start_datetime','end_datetime',"slot_configuration_id")
    def _compute_name(self):
        for r in self:
            if r.slot_configuration_id and r.start_datetime and r.end_datetime:
                r.name = (r.slot_configuration_id.product_id.name + ' : ' +
                          str(r.start_datetime+timedelta(hours=UTC_HOURS))+' - > '+str(r.end_datetime+timedelta(hours=UTC_HOURS)))
