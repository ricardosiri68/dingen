from marshmallow import Schema, fields

class EntrySchema (Schema):
    id = fields.Int()
    title = fields.Str()
    body_html = fields.Str()
