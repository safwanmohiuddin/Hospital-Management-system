from odoo import api, fields, models #keep 2 lines empty after this

class HospitalAppointment(models.Model):
    _name = "hospital.appointment" #Name should have .
    _description = "Appointment Details"
    _rec_names_search = ['reference','patient_id']
    _rec_name = 'patient_id'

    reference = fields.Char(string = "Reference", default = "New")
    patient_id = fields.Many2one('hospital.patient', string = "Patient", ondelete = 'restrict')
    date_appointment = fields.Date(string = "Date")
    note = fields.Text(string = "note")
    state = fields.Selection([('draft','Draft'),('confirmed','Confirmed'),
                              ('ongoing','Ongoing'),('done','Done'),('cancel','Cancel')], default = "draft")
    appointment_lines_ids = fields.One2many('hospital.appointment.line','appointment_id',string = "lines")
    total_qty = fields.Float(compute = '_compute_total_qty' ,string="Quantity", store = True)
    patient_dob = fields.Date(string = "Date of Birth", related = 'patient_id.date_of_birth') #related field


    @api.model_create_multi
    def create(self, vals_list):  #vals_list is a dictionary
        print("odoo mates", vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)

    @api.depends('appointment_lines_ids','appointment_lines_ids.qty')
    def _compute_total_qty(self):
        for rec in self:
            rec.total_qty = sum(rec.appointment_lines_ids.mapped('qty'))
            # for line in rec.appointment_lines_ids:
            #     print("line: ", line.qty)
            #     total_qty = total_qty + line.qtyx
            # rec.total_qty = total_qty


    def _compute_display_name(self):     #this is how this model will be shown, in the other model which referenced this model in their many2one field
        for rec in self:
            rec.display_name = f"[{rec.reference}]{rec.patient_id.name}"

    def action_confirm(self):     #This is for the buttons in header
        for rec in self:
            rec.state = "confirmed"


    def action_ongoing(self):
        for rec in self:
            rec.state = "ongoing"


    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancelled(self):
        for rec in self:
            rec.state = "cancel"

    class HospitalAppointmentLine(models.Model):
        _name = "hospital.appointment.line"  # Name should have .
        _description = "Appointment Details Line"

        appointment_id  = fields.Many2one('hospital.appointment', string = "Appointment")
        product_id = fields.Many2one('product.product', string = "Product", required = True)
        qty = fields.Float(string = "Quantity")








