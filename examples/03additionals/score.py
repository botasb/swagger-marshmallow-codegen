# -*- coding:utf-8 -*-
# this is auto-generated by swagger-marshmallow-codegen
from marshmallow import (
    Schema,
    fields
)
from swagger_marshmallow_codegen.schema import AdditionalPropertiesSchema


class Score(AdditionalPropertiesSchema):
    name = fields.String(required=True)

    class Meta:
        additional_field = fields.Integer()
