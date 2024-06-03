from odoo import fields, models, api


class Reservation(models.Model):
    # _name = 'activity.slot.reservation'
    # _description = 'Activity Slot Reservation'
    _inherit='calendar.event'
    first_name=fields.Char(string='Name', required=True)
    middle_name=fields.Char(string='Name', required=True)
    last_name=fields.Char(string='Name', required=True)
    # slot_id=fields.Many2one('activity.slot.configuration',string='Slot')
    # reservation_date=fields.Datetime(default=lambda self:fields.Datetime.now(), string='Reservation time')
    paid=fields.Boolean(string='Paid')
    mobile=fields.Char(string='Mobile')
    email=fields.Char(string='Email')

    name=fields.Char(string='Name',compute='_compute_name',store=True)

    # @api.depends('first_name','last_name','slot_id')
    # def _compute_name(self):
    #     for r in self:
    #         if (r.slot_id and
    #                 r.first_name and r.last_name):
    #             r.name = (r.first_name + ' ' + r.last_name + ' -> '+
    #                       r.slot_id.name)