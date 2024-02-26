from odoo import models, fields


class Modulo(models.Model):
    _name = 'cicloformativo_amf.modulo'
    _description = 'Módulo'

    nombremod = fields.Char(string='Nombre', required=True)
    ciclo_id = fields.Many2one('cicloformativo_amf.cicloformativo', string='Ciclo Formativo', required=True)
    alumno_ids = fields.Many2many('cicloformativo_amf.alumno', string='Alumnos Matriculados')
    profesor_id = fields.Many2one('cicloformativo_amf.profesor', string='Profesor')
