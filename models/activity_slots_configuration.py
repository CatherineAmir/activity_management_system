from odoo import fields, models, api


class ActivitySlots(models.Model):
    # _name = 'activity.slot.configuration'
    _inherit="appointment.type"
    name=fields.Char(string='Name',compute='_compute_name',store=True)
    product_id=fields.Many2one('product.template',ondelete='cascade',string='Activity',auto_join=True)
    # state = fields.Selection([('draft','Draft'),('open','Open'),('closed','Closed')])
    max_number=fields.Integer(string="Max Reservations For this Slot")
    close_all_booking=fields.Boolean(default=False)
    start_date=fields.Date(string="Start Date",required=True,help="start date where this configuration is working")
    end_date=fields.Date(string="End Date",required=False,help="End date where this configuration is not working")

    # start_time=fields.Float(string='Start Time')
    # end_time=fields.Float(string='End Time')
    # duration=fields.Integer(string='Duration',required=True)
    time_interval=fields.Selection([('minutes','Minutes'),('hours','Hours'),('days','Days')])


    # repeating of slots
    interval_number=fields.Integer(string='Create Slot Duration')
    interval_type=fields.Selection([('minutes','Minutes'),("hours","Hours"),("days","Days")])
    location=fields.Char(string="Location",related='product_id.location',store=1)
    city=fields.Char(string="City",related='product_id.city',store=1)
    @api.depends('start_date', 'end_date', "product_id")
    def _compute_name(self):
        for r in self:
            if r.product_id :
                    # and r.start_date and r.end_date):
                r.name = r.product_id.name
                # + ' : ' +
                #           str(r.start_date)+' - > '+str(r.end_date))

    # @api.depends('duration', 'time_interval','start_time')
    # def _compute_end_time(self):