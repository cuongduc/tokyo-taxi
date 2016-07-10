# -*- encoding: utf-8 -*-
import sys
from wtforms import Form, StringField, DecimalField, SelectField, HiddenField

reload(sys)
sys.setdefaultencoding("utf-8")


class ParcelRequestForm(Form):
    parcel_type = SelectField('Loại hàng hóa', choices=[(
        'Đồ điện tử', 'Đồ điện tử'), ('Đồ gia dụng', 'Đồ gia dụng'),
        ('Hải sản', 'Hải sản'), ('Rau củ quả', 'Rau củ quả'),
        ('Bưu kiện', 'Bưu kiện')])
    parcel_weight = StringField('Khối lượng')
    parcel_dimension = StringField('Kích thước')
    parcel_arrive_time = SelectField('Thời gian nhận', choices=[
        ('12h đến 2h', '12h đến 2h'), ('2h đến 4h', '2h đến 4h'),
        ('4h đến 6h', '4h đến 6h'), ('6h đến 8h', '6h đến 8h'),
        ('8h đến 12h', '8h đến 12h')])
    parcel_fee = DecimalField('Tiền thu hộ')
    parcel_note = StringField('Ghi chú')
    parcel_place = HiddenField('parcel_place')
