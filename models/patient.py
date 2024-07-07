# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalPatient(models.Model):
    _name = "hospital.patient"  # name of the table "hospital_patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    gender = fields.Selection(string="Gender", selection=[("male", "Male"), ("female", "Female")])
