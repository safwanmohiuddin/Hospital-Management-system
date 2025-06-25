from odoo import api, fields, models #keep 2 lines empty after this

class HospitalPatientTag(models.Model):
    _name = "hospital.patient.tag" #Name should have .
    _description = "Patient Tag"
    _order = 'sequence,id'

    name = fields.Char(string = "Name", required = True)
    sequence = fields.Integer(default = 10)
