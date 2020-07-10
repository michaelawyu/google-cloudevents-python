# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/events/cloud/pubsub/v1/data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/events/cloud/pubsub/v1/data.proto',
  package='google.events.cloud.pubsub.v1',
  syntax='proto3',
  serialized_options=b'\252\002&Google.Events.Protobuf.Cloud.PubSub.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(google/events/cloud/pubsub/v1/data.proto\x12\x1dgoogle.events.cloud.pubsub.v1\"k\n\x14MessagePublishedData\x12=\n\x07message\x18\x01 \x01(\x0b\x32,.google.events.cloud.pubsub.v1.PubsubMessage\x12\x14\n\x0csubscription\x18\x02 \x01(\t\"\xb6\x01\n\rPubsubMessage\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12P\n\nattributes\x18\x02 \x03(\x0b\x32<.google.events.cloud.pubsub.v1.PubsubMessage.AttributesEntry\x12\x12\n\nmessage_id\x18\x03 \x01(\t\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42)\xaa\x02&Google.Events.Protobuf.Cloud.PubSub.V1b\x06proto3'
)




_MESSAGEPUBLISHEDDATA = _descriptor.Descriptor(
  name='MessagePublishedData',
  full_name='google.events.cloud.pubsub.v1.MessagePublishedData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='google.events.cloud.pubsub.v1.MessagePublishedData.message', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subscription', full_name='google.events.cloud.pubsub.v1.MessagePublishedData.subscription', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=182,
)


_PUBSUBMESSAGE_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='google.events.cloud.pubsub.v1.PubsubMessage.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.events.cloud.pubsub.v1.PubsubMessage.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.events.cloud.pubsub.v1.PubsubMessage.AttributesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=318,
  serialized_end=367,
)

_PUBSUBMESSAGE = _descriptor.Descriptor(
  name='PubsubMessage',
  full_name='google.events.cloud.pubsub.v1.PubsubMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.events.cloud.pubsub.v1.PubsubMessage.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='google.events.cloud.pubsub.v1.PubsubMessage.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='google.events.cloud.pubsub.v1.PubsubMessage.message_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PUBSUBMESSAGE_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=367,
)

_MESSAGEPUBLISHEDDATA.fields_by_name['message'].message_type = _PUBSUBMESSAGE
_PUBSUBMESSAGE_ATTRIBUTESENTRY.containing_type = _PUBSUBMESSAGE
_PUBSUBMESSAGE.fields_by_name['attributes'].message_type = _PUBSUBMESSAGE_ATTRIBUTESENTRY
DESCRIPTOR.message_types_by_name['MessagePublishedData'] = _MESSAGEPUBLISHEDDATA
DESCRIPTOR.message_types_by_name['PubsubMessage'] = _PUBSUBMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessagePublishedData = _reflection.GeneratedProtocolMessageType('MessagePublishedData', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEPUBLISHEDDATA,
  '__module__' : 'google.events.cloud.pubsub.v1.data_pb2'
  # @@protoc_insertion_point(class_scope:google.events.cloud.pubsub.v1.MessagePublishedData)
  })
_sym_db.RegisterMessage(MessagePublishedData)

PubsubMessage = _reflection.GeneratedProtocolMessageType('PubsubMessage', (_message.Message,), {

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _PUBSUBMESSAGE_ATTRIBUTESENTRY,
    '__module__' : 'google.events.cloud.pubsub.v1.data_pb2'
    # @@protoc_insertion_point(class_scope:google.events.cloud.pubsub.v1.PubsubMessage.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _PUBSUBMESSAGE,
  '__module__' : 'google.events.cloud.pubsub.v1.data_pb2'
  # @@protoc_insertion_point(class_scope:google.events.cloud.pubsub.v1.PubsubMessage)
  })
_sym_db.RegisterMessage(PubsubMessage)
_sym_db.RegisterMessage(PubsubMessage.AttributesEntry)


DESCRIPTOR._options = None
_PUBSUBMESSAGE_ATTRIBUTESENTRY._options = None
# @@protoc_insertion_point(module_scope)