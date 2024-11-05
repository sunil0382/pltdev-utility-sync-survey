# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: customer_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 27, 2, "", "customer_service.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16\x63ustomer_service.proto\x12\x0cgrpc_service\x1a\x1cgoogle/api/annotations.proto"\x0e\n\x0c\x45mptyRequest"7\n\x14ListCustomersRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05")\n\x12GetCustomerRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\x05"\xbe\x01\n\x13\x43ustomerInformation\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\x05\x12\x15\n\rfirst_name_en\x18\x02 \x01(\t\x12\x14\n\x0clast_name_en\x18\x03 \x01(\t\x12\x1e\n\x16primary_contact_number\x18\x04 \x01(\t\x12\x45\n\x18utility_service_requests\x18\x05 \x03(\x0b\x32#.grpc_service.UtilityServiceRequest"s\n\x15UtilityServiceRequest\x12\x1a\n\x12utility_request_id\x18\x01 \x01(\x05\x12\x16\n\x0eutility_number\x18\x02 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x03 \x01(\x05\x12\x0e\n\x06region\x18\x04 \x01(\t"J\n\x13GetCustomerResponse\x12\x33\n\x08\x63ustomer\x18\x01 \x01(\x0b\x32!.grpc_service.CustomerInformation"{\n\x08\x43ustomer\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\x05\x12\x15\n\rfirst_name_en\x18\x02 \x01(\t\x12\x14\n\x0clast_name_en\x18\x03 \x01(\t\x12\x1e\n\x16primary_contact_number\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t"w\n\x14\x43ustomerListResponse\x12)\n\tcustomers\x18\x01 \x03(\x0b\x32\x16.grpc_service.Customer\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x32\xfa\x01\n\x0f\x43ustomerService\x12n\n\rListCustomers\x12".grpc_service.ListCustomersRequest\x1a".grpc_service.CustomerListResponse"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/v1/customers\x12w\n\x0bGetCustomer\x12 .grpc_service.GetCustomerRequest\x1a!.grpc_service.GetCustomerResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/customers/{customer_id}B\x1eZ\x1cus-api/grpc_service/customerb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "customer_service_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z\034us-api/grpc_service/customer"
    _globals["_CUSTOMERSERVICE"].methods_by_name["ListCustomers"]._loaded_options = None
    _globals["_CUSTOMERSERVICE"].methods_by_name[
        "ListCustomers"
    ]._serialized_options = b"\202\323\344\223\002\017\022\r/v1/customers"
    _globals["_CUSTOMERSERVICE"].methods_by_name["GetCustomer"]._loaded_options = None
    _globals["_CUSTOMERSERVICE"].methods_by_name[
        "GetCustomer"
    ]._serialized_options = (
        b"\202\323\344\223\002\035\022\033/v1/customers/{customer_id}"
    )
    _globals["_EMPTYREQUEST"]._serialized_start = 70
    _globals["_EMPTYREQUEST"]._serialized_end = 84
    _globals["_LISTCUSTOMERSREQUEST"]._serialized_start = 86
    _globals["_LISTCUSTOMERSREQUEST"]._serialized_end = 141
    _globals["_GETCUSTOMERREQUEST"]._serialized_start = 143
    _globals["_GETCUSTOMERREQUEST"]._serialized_end = 184
    _globals["_CUSTOMERINFORMATION"]._serialized_start = 187
    _globals["_CUSTOMERINFORMATION"]._serialized_end = 377
    _globals["_UTILITYSERVICEREQUEST"]._serialized_start = 379
    _globals["_UTILITYSERVICEREQUEST"]._serialized_end = 494
    _globals["_GETCUSTOMERRESPONSE"]._serialized_start = 496
    _globals["_GETCUSTOMERRESPONSE"]._serialized_end = 570
    _globals["_CUSTOMER"]._serialized_start = 572
    _globals["_CUSTOMER"]._serialized_end = 695
    _globals["_CUSTOMERLISTRESPONSE"]._serialized_start = 697
    _globals["_CUSTOMERLISTRESPONSE"]._serialized_end = 816
    _globals["_CUSTOMERSERVICE"]._serialized_start = 819
    _globals["_CUSTOMERSERVICE"]._serialized_end = 1069
# @@protoc_insertion_point(module_scope)
