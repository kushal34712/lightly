# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from lightly.openapi_generated.swagger_client.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class SamplingConfig(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    
    class stoppingCondition(
        DictSchema
    ):
        nSamples = NumberSchema
        minDistance = NumberSchema
    
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, ],
            nSamples: typing.Union[nSamples, Unset] = unset,
            minDistance: typing.Union[minDistance, Unset] = unset,
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'stoppingCondition':
            return super().__new__(
                cls,
                *args,
                nSamples=nSamples,
                minDistance=minDistance,
                _configuration=_configuration,
                **kwargs,
            )


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        stoppingCondition: typing.Union[stoppingCondition, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'SamplingConfig':
        return super().__new__(
            cls,
            *args,
            stoppingCondition=stoppingCondition,
            _configuration=_configuration,
            **kwargs,
        )
