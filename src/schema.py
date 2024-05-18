from marshmallow import Schema, fields


class SnomedCodeSchema(Schema):
    concept_id = fields.String()
    description_id = fields.String()
    description = fields.String()


class SearchInputSchema(Schema):
    n = fields.Integer()
    search_string = fields.String()