# -*- coding:utf-8 -*-
# this is auto-generated by swagger-marshmallow-codegen
from marshmallow import (
    Schema,
    fields
)
from swagger_marshmallow_codegen.schema import (
    PrimitiveValueSchema
)


class IdsInput:
    class Get:
        pass



class IdsIdInput:
    class Get:
        pass



class IdsOutput:
    class Get200(PrimitiveValueSchema):
        class schema_class(Schema):
            value = fields.List(fields.Integer())




class IdsIdOutput:
    class Get200(PrimitiveValueSchema):
        class schema_class(Schema):
            value = fields.Integer()
