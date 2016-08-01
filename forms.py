# -*- encoding: utf-8 -*-
import sys
from wtforms import Form, StringField, DecimalField, SelectField, HiddenField

reload(sys)
sys.setdefaultencoding("utf-8")


class ParcelRequestForm(Form):
    parcel_type = SelectField('Parcel type', choices=[(
        'Electronics', 'Electronics'),
        ('Household appliances', 'Household appliances'),
        ('Seafood', 'Seafood'), ('Food and Beverage', 'Food and Beverage'),
        ('Express package', 'Express package')])
    parcel_weight = StringField('Weight')
    parcel_dimension = StringField('Size')
    parcel_arrive_time = SelectField('Received time', choices=[
        ('12h đến 2h', '12h đến 2h'), ('2h đến 4h', '2h đến 4h'),
        ('4h đến 6h', '4h đến 6h'), ('6h đến 8h', '6h đến 8h'),
        ('8h đến 12h', '8h đến 12h')])
    parcel_fee = DecimalField('Package fee')
    parcel_note = StringField('Note')
    parcel_place = HiddenField('parcel_place')
