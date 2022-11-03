# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='person.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cperson.proto\"X\n\rPersonMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t\"4\n\x11PersonMessageList\x12\x1f\n\x07persons\x18\x01 \x03(\x0b\x32\x0e.PersonMessage\"\x07\n\x05\x45mpty22\n\rPersonService\x12!\n\x03Get\x12\x06.Empty\x1a\x12.PersonMessageListb\x06proto3'
)




_PERSONMESSAGE = _descriptor.Descriptor(
  name='PersonMessage',
  full_name='PersonMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PersonMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='PersonMessage.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='PersonMessage.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_name', full_name='PersonMessage.company_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=16,
  serialized_end=104,
)


_PERSONMESSAGELIST = _descriptor.Descriptor(
  name='PersonMessageList',
  full_name='PersonMessageList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='persons', full_name='PersonMessageList.persons', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=106,
  serialized_end=158,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=160,
  serialized_end=167,
)

_PERSONMESSAGELIST.fields_by_name['persons'].message_type = _PERSONMESSAGE
DESCRIPTOR.message_types_by_name['PersonMessage'] = _PERSONMESSAGE
DESCRIPTOR.message_types_by_name['PersonMessageList'] = _PERSONMESSAGELIST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PersonMessage = _reflection.GeneratedProtocolMessageType('PersonMessage', (_message.Message,), {
  'DESCRIPTOR' : _PERSONMESSAGE,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:PersonMessage)
  })
_sym_db.RegisterMessage(PersonMessage)

PersonMessageList = _reflection.GeneratedProtocolMessageType('PersonMessageList', (_message.Message,), {
  'DESCRIPTOR' : _PERSONMESSAGELIST,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:PersonMessageList)
  })
_sym_db.RegisterMessage(PersonMessageList)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)



_PERSONSERVICE = _descriptor.ServiceDescriptor(
  name='PersonService',
  full_name='PersonService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=169,
  serialized_end=219,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='PersonService.Get',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_PERSONMESSAGELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PERSONSERVICE)

DESCRIPTOR.services_by_name['PersonService'] = _PERSONSERVICE

# @@protoc_insertion_point(module_scope)
