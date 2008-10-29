#!/usr/bin/python2.4
# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2


_ACCESSPROFILE_ACCESSSCHEME = descriptor.EnumDescriptor(
  name='AccessScheme',
  full_name='sae.AccessProfile.AccessScheme',
  filename='AccessScheme',
  values=[
    descriptor.EnumValueDescriptor(
      name='TELNET', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SSH', index=1, number=1,
      options=None,
      type=None),
  ],
  options=None,
)


_ERROR = descriptor.Descriptor(
  name='Error',
  full_name='sae.Error',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='error', full_name='sae.Error.error', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='sae.Error.message', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_MESSAGE = descriptor.Descriptor(
  name='Message',
  full_name='sae.Message',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='transaction_id', full_name='sae.Message.transaction_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='method', full_name='sae.Message.method', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='request', full_name='sae.Message.request', index=2,
      number=3, type=12, cpp_type=9, label=1,
      default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='response', full_name='sae.Message.response', index=3,
      number=4, type=12, cpp_type=9, label=1,
      default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='error', full_name='sae.Message.error', index=4,
      number=5, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_ACCESSPROFILE = descriptor.Descriptor(
  name='AccessProfile',
  full_name='sae.AccessProfile',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='scheme', full_name='sae.AccessProfile.scheme', index=0,
      number=1, type=14, cpp_type=8, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='address', full_name='sae.AccessProfile.address', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='port', full_name='sae.AccessProfile.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user', full_name='sae.AccessProfile.user', index=3,
      number=4, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='password', full_name='sae.AccessProfile.password', index=4,
      number=5, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='super_password', full_name='sae.AccessProfile.super_password', index=5,
      number=6, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='path', full_name='sae.AccessProfile.path', index=6,
      number=7, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
    _ACCESSPROFILE_ACCESSSCHEME,
  ],
  options=None)


_REQREGISTER = descriptor.Descriptor(
  name='ReqRegister',
  full_name='sae.ReqRegister',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='sae.ReqRegister.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_RESREGISTER = descriptor.Descriptor(
  name='ResRegister',
  full_name='sae.ResRegister',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='version', full_name='sae.ResRegister.version', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_REQPULLCONFIG = descriptor.Descriptor(
  name='ReqPullConfig',
  full_name='sae.ReqPullConfig',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='access_profile', full_name='sae.ReqPullConfig.access_profile', index=0,
      number=1, type=11, cpp_type=10, label=2,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='profile', full_name='sae.ReqPullConfig.profile', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_RESPULLCONFIG = descriptor.Descriptor(
  name='ResPullConfig',
  full_name='sae.ResPullConfig',
  filename='sae.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='config', full_name='sae.ResPullConfig.config', index=0,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_MESSAGE.fields_by_name['error'].message_type = _ERROR
_ACCESSPROFILE.fields_by_name['scheme'].enum_type = _ACCESSPROFILE_ACCESSSCHEME
_REQPULLCONFIG.fields_by_name['access_profile'].message_type = _ACCESSPROFILE

class Error(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ERROR

class Message(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MESSAGE

class AccessProfile(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACCESSPROFILE

class ReqRegister(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQREGISTER

class ResRegister(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESREGISTER

class ReqPullConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQPULLCONFIG

class ResPullConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPULLCONFIG

