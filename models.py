# -*- coding: utf-8 -*-
from odoo import models, fields, api


class TestModel(models.Model):
    _name = 'test_model'

    name = fields.Char(string='姓名')
    age = fields.Integer(string='年龄')
    birth = fields.Date(string='出生日期')
