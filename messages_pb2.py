# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0emessages.proto\"\xd7\x03\n\x06Record\x12\x0e\n\x06WBANNO\x18\x01 \x01(\x03\x12\x10\n\x08UTC_DATE\x18\x02 \x01(\x03\x12\x10\n\x08UTC_TIME\x18\x03 \x01(\x03\x12\x10\n\x08LST_DATE\x18\x04 \x01(\x03\x12\x10\n\x08LST_TIME\x18\x05 \x01(\x03\x12\x0e\n\x06\x43RX_VN\x18\x06 \x01(\x03\x12\x11\n\tLONGITUDE\x18\x07 \x01(\x02\x12\x10\n\x08LATITUDE\x18\x08 \x01(\x02\x12\x17\n\x0f\x41IR_TEMPERATURE\x18\t \x01(\x02\x12\x15\n\rPRECIPITATION\x18\n \x01(\x02\x12\x17\n\x0fSOLAR_RADIATION\x18\x0b \x01(\x02\x12\x0f\n\x07SR_FLAG\x18\x0c \x01(\x03\x12\x1b\n\x13SURFACE_TEMPERATURE\x18\r \x01(\x02\x12\x0f\n\x07ST_TYPE\x18\x0e \x01(\t\x12\x0f\n\x07ST_FLAG\x18\x0f \x01(\x03\x12\x19\n\x11RELATIVE_HUMIDITY\x18\x10 \x01(\x03\x12\x0f\n\x07RH_FLAG\x18\x11 \x01(\x03\x12\x17\n\x0fSOIL_MOISTURE_5\x18\x12 \x01(\x02\x12\x1a\n\x12SOIL_TEMPERATURE_5\x18\x13 \x01(\x02\x12\x0f\n\x07WETNESS\x18\x14 \x01(\x03\x12\x10\n\x08WET_FLAG\x18\x15 \x01(\x03\x12\x10\n\x08WIND_1_5\x18\x16 \x01(\x02\x12\x11\n\tWIND_FLAG\x18\x17 \x01(\x03\" \n\x05\x42\x61tch\x12\x17\n\x06record\x18\x01 \x03(\x0b\x32\x07.Recordb\x06proto3')
)



_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='WBANNO', full_name='Record.WBANNO', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='UTC_DATE', full_name='Record.UTC_DATE', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='UTC_TIME', full_name='Record.UTC_TIME', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LST_DATE', full_name='Record.LST_DATE', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LST_TIME', full_name='Record.LST_TIME', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CRX_VN', full_name='Record.CRX_VN', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LONGITUDE', full_name='Record.LONGITUDE', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LATITUDE', full_name='Record.LATITUDE', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='AIR_TEMPERATURE', full_name='Record.AIR_TEMPERATURE', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PRECIPITATION', full_name='Record.PRECIPITATION', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SOLAR_RADIATION', full_name='Record.SOLAR_RADIATION', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SR_FLAG', full_name='Record.SR_FLAG', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SURFACE_TEMPERATURE', full_name='Record.SURFACE_TEMPERATURE', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ST_TYPE', full_name='Record.ST_TYPE', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ST_FLAG', full_name='Record.ST_FLAG', index=14,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RELATIVE_HUMIDITY', full_name='Record.RELATIVE_HUMIDITY', index=15,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RH_FLAG', full_name='Record.RH_FLAG', index=16,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SOIL_MOISTURE_5', full_name='Record.SOIL_MOISTURE_5', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SOIL_TEMPERATURE_5', full_name='Record.SOIL_TEMPERATURE_5', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='WETNESS', full_name='Record.WETNESS', index=19,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='WET_FLAG', full_name='Record.WET_FLAG', index=20,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='WIND_1_5', full_name='Record.WIND_1_5', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='WIND_FLAG', full_name='Record.WIND_FLAG', index=22,
      number=23, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=490,
)


_BATCH = _descriptor.Descriptor(
  name='Batch',
  full_name='Batch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='Batch.record', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=524,
)

_BATCH.fields_by_name['record'].message_type = _RECORD
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['Batch'] = _BATCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), dict(
  DESCRIPTOR = _RECORD,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Record)
  ))
_sym_db.RegisterMessage(Record)

Batch = _reflection.GeneratedProtocolMessageType('Batch', (_message.Message,), dict(
  DESCRIPTOR = _BATCH,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Batch)
  ))
_sym_db.RegisterMessage(Batch)


# @@protoc_insertion_point(module_scope)
