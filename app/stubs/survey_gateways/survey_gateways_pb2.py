# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: survey_gateways.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 27, 2, "", "survey_gateways.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15survey_gateways.proto\x12\x14grpc_service.utility"\x9a\x02\n\x0eSurveyGateways\x12\x14\n\x0cgateway_type\x18\x01 \x01(\t\x12\x18\n\x10gateway_scenario\x18\x02 \x01(\t\x12\x14\n\x0c\x63\x61\x62le_length\x18\x03 \x01(\x02\x12\x0c\n\x04room\x18\x04 \x01(\t\x12\x17\n\x0f\x63onnection_type\x18\x05 \x01(\t\x12\x12\n\nmodel_name\x18\x06 \x01(\t\x12\x0c\n\x04slug\x18\x07 \x01(\t\x12\x12\n\nfloor_code\x18\x08 \x01(\t\x12\x10\n\x08\x66loor_id\x18\t \x01(\x03\x12\x1a\n\x12power_interruption\x18\n \x01(\x08\x12\x17\n\x0fsignal_strength\x18\x0b \x01(\x02\x12\x0f\n\x07\x61ntenna\x18\x0c \x01(\x08\x12\r\n\x05label\x18\r \x01(\tb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "survey_gateways_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_SURVEYGATEWAYS"]._serialized_start = 48
    _globals["_SURVEYGATEWAYS"]._serialized_end = 330
# @@protoc_insertion_point(module_scope)
