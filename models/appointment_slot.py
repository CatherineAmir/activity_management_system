from odoo import fields, models, api


class AppointmentSlots(models.Model):
    _inherit='appointment.slot'
    max_number = fields.Integer(string="Max Reservations Slot",related='appointment_type_id.max_number',store=1)
    available_number = fields.Integer(string="Availability")



