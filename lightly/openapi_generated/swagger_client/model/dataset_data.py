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


class DatasetData(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'id',
        'name',
        'userId',
        'type',
        'nSamples',
        'sizeInBytes',
        'createdAt',
        'lastModifiedAt',
    ))

    @classmethod
    @property
    def id(cls) -> typing.Type['MongoObjectID']:
        return MongoObjectID

    @classmethod
    @property
    def name(cls) -> typing.Type['DatasetName']:
        return DatasetName
    userId = StrSchema

    @classmethod
    @property
    def accessType(cls) -> typing.Type['SharedAccessType']:
        return SharedAccessType

    @classmethod
    @property
    def type(cls) -> typing.Type['DatasetType']:
        return DatasetType

    @classmethod
    @property
    def imgType(cls) -> typing.Type['ImageType']:
        return ImageType
    nSamples = Int32Schema
    sizeInBytes = Int64Schema

    @classmethod
    @property
    def metaDataConfigurationId(cls) -> typing.Type['MongoObjectID']:
        return MongoObjectID

    @classmethod
    @property
    def createdAt(cls) -> typing.Type['Timestamp']:
        return Timestamp

    @classmethod
    @property
    def lastModifiedAt(cls) -> typing.Type['Timestamp']:
        return Timestamp

    @classmethod
    @property
    def datasourceProcessedUntilTimestamp(cls) -> typing.Type['TimestampSeconds']:
        return TimestampSeconds

    @classmethod
    @property
    def accessRole(cls) -> typing.Type['AccessRole']:
        return AccessRole

    @classmethod
    @property
    def parentDatasetId(cls) -> typing.Type['MongoObjectID']:
        return MongoObjectID


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        id: id,
        name: name,
        userId: userId,
        type: type,
        nSamples: nSamples,
        sizeInBytes: sizeInBytes,
        createdAt: createdAt,
        lastModifiedAt: lastModifiedAt,
        accessType: typing.Union['SharedAccessType', Unset] = unset,
        imgType: typing.Union['ImageType', Unset] = unset,
        metaDataConfigurationId: typing.Union['MongoObjectID', Unset] = unset,
        datasourceProcessedUntilTimestamp: typing.Union['TimestampSeconds', Unset] = unset,
        accessRole: typing.Union['AccessRole', Unset] = unset,
        parentDatasetId: typing.Union['MongoObjectID', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'DatasetData':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            userId=userId,
            type=type,
            nSamples=nSamples,
            sizeInBytes=sizeInBytes,
            createdAt=createdAt,
            lastModifiedAt=lastModifiedAt,
            accessType=accessType,
            imgType=imgType,
            metaDataConfigurationId=metaDataConfigurationId,
            datasourceProcessedUntilTimestamp=datasourceProcessedUntilTimestamp,
            accessRole=accessRole,
            parentDatasetId=parentDatasetId,
            _configuration=_configuration,
            **kwargs,
        )

from lightly.openapi_generated.swagger_client.model.access_role import AccessRole
from lightly.openapi_generated.swagger_client.model.dataset_name import DatasetName
from lightly.openapi_generated.swagger_client.model.dataset_type import DatasetType
from lightly.openapi_generated.swagger_client.model.image_type import ImageType
from lightly.openapi_generated.swagger_client.model.mongo_object_id import MongoObjectID
from lightly.openapi_generated.swagger_client.model.shared_access_type import SharedAccessType
from lightly.openapi_generated.swagger_client.model.timestamp import Timestamp
from lightly.openapi_generated.swagger_client.model.timestamp_seconds import TimestampSeconds
