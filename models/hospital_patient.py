from xml.dom import VALIDATION_ERR

from odoo import api, fields, models,_
from odoo.exceptions import ValidationError
 #keep 2 lines empty after this

class HospitalPatient(models.Model):
    _name = "hospital.patient" #Name should have .
    _description = "Patient Master"
    _rec_name = "name"

    name = fields.Char(string = "Name", required = True)
    date_of_birth = fields.Date(string = "Date of Birth")
    gender = fields.Selection([('male', 'Male'), ('female','Female'),], string = "Gender")
    tag_id = fields.Many2many('hospital.patient.tag','patient_tag_rel','patient_id','tag_id', string="Tags")

    def unlink(self):
        for rec in self:
            print("Super method is exececuted")
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise ValidationError(_('The Appointment record needs to be deleted too'))
        return super().unlink()
