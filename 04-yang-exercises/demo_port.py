# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class yc_config_demo_port__ports_port_config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module demo-port - based on the path /ports/port/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for a port
  """
  __slots__ = ('_path_helper', '_extmethods', '__speed',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__speed = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'SPEED_10GB': {'@module': 'demo-port', '@namespace': 'https://opennetworking.org/yang/demo'}, 'demo-port:SPEED_10GB': {'@module': 'demo-port', '@namespace': 'https://opennetworking.org/yang/demo'}},), is_leaf=True, yang_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='identityref', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['ports', 'port', 'config']

  def _get_speed(self):
    """
    Getter method for speed, mapped from YANG variable /ports/port/config/speed (identityref)

    YANG Description: Configurable speed of a switch port
    """
    return self.__speed
      
  def _set_speed(self, v, load=False):
    """
    Setter method for speed, mapped from YANG variable /ports/port/config/speed (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_speed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_speed() directly.

    YANG Description: Configurable speed of a switch port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'SPEED_10GB': {'@module': 'demo-port', '@namespace': 'https://opennetworking.org/yang/demo'}, 'demo-port:SPEED_10GB': {'@module': 'demo-port', '@namespace': 'https://opennetworking.org/yang/demo'}},), is_leaf=True, yang_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """speed must be of a type compatible with identityref""",
          'defined-type': "demo-port:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'SPEED_10GB': {'@module': 'demo-port', '@namespace': 'https://opennetworking.org/yang/demo'}, 'demo-port:SPEED_10GB': {'@module': 'demo-port', '@namespace': 'https://opennetworking.org/yang/demo'}},), is_leaf=True, yang_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='identityref', is_config=True)""",
        })

    self.__speed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_speed(self):
    self.__speed = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'SPEED_10GB': {'@module': 'demo-port', '@namespace': 'https://opennetworking.org/yang/demo'}, 'demo-port:SPEED_10GB': {'@module': 'demo-port', '@namespace': 'https://opennetworking.org/yang/demo'}},), is_leaf=True, yang_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='identityref', is_config=True)

  speed = __builtin__.property(_get_speed, _set_speed)


  _pyangbind_elements = OrderedDict([('speed', speed), ])


class yc_state_demo_port__ports_port_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module demo-port - based on the path /ports/port/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Read-only state for a port
  """
  __slots__ = ('_path_helper', '_extmethods', '__status',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='boolean', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['ports', 'port', 'state']

  def _get_status(self):
    """
    Getter method for status, mapped from YANG variable /ports/port/state/status (boolean)

    YANG Description: Number
    """
    return self.__status
      
  def _set_status(self, v, load=False):
    """
    Setter method for status, mapped from YANG variable /ports/port/state/status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_status() directly.

    YANG Description: Number
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='boolean', is_config=False)""",
        })

    self.__status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_status(self):
    self.__status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='boolean', is_config=False)

  status = __builtin__.property(_get_status)


  _pyangbind_elements = OrderedDict([('status', status), ])


class yc_port_demo_port__ports_port(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module demo-port - based on the path /ports/port. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of ports on a switch
  """
  __slots__ = ('_path_helper', '_extmethods', '__port_number','__config','__state',)

  _yang_name = 'port'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__port_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..32']}), is_leaf=True, yang_name="port-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='port-number', is_config=True)
    self.__config = YANGDynClass(base=yc_config_demo_port__ports_port_config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=yc_state_demo_port__ports_port_state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['ports', 'port']

  def _get_port_number(self):
    """
    Getter method for port_number, mapped from YANG variable /ports/port/port_number (port-number)

    YANG Description: Port number (maps to the front panel port of a switch); also the key for the port list
    """
    return self.__port_number
      
  def _set_port_number(self, v, load=False):
    """
    Setter method for port_number, mapped from YANG variable /ports/port/port_number (port-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_number() directly.

    YANG Description: Port number (maps to the front panel port of a switch); also the key for the port list
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..32']}), is_leaf=True, yang_name="port-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='port-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_number must be of a type compatible with port-number""",
          'defined-type': "demo-port:port-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..32']}), is_leaf=True, yang_name="port-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='port-number', is_config=True)""",
        })

    self.__port_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_number(self):
    self.__port_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..32']}), is_leaf=True, yang_name="port-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='port-number', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /ports/port/config (container)

    YANG Description: Configuration data for a port
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /ports/port/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for a port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_config_demo_port__ports_port_config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_config_demo_port__ports_port_config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=yc_config_demo_port__ports_port_config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /ports/port/state (container)

    YANG Description: Read-only state for a port
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /ports/port/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Read-only state for a port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_state_demo_port__ports_port_state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_state_demo_port__ports_port_state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=yc_state_demo_port__ports_port_state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)

  port_number = __builtin__.property(_get_port_number, _set_port_number)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)


  _pyangbind_elements = OrderedDict([('port_number', port_number), ('config', config), ('state', state), ])


class yc_ports_demo_port__ports(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module demo-port - based on the path /ports. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The root container for port configuration and state
  """
  __slots__ = ('_path_helper', '_extmethods', '__port',)

  _yang_name = 'ports'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__port = YANGDynClass(base=YANGListType("port_number",yc_port_demo_port__ports_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-number', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['ports']

  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /ports/port (list)

    YANG Description: List of ports on a switch
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /ports/port (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.

    YANG Description: List of ports on a switch
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("port_number",yc_port_demo_port__ports_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-number', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("port_number",yc_port_demo_port__ports_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-number', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='list', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=YANGListType("port_number",yc_port_demo_port__ports_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-number', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='list', is_config=True)

  port = __builtin__.property(_get_port, _set_port)


  _pyangbind_elements = OrderedDict([('port', port), ])


class demo_port(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module demo-port - based on the path /demo-port. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Demo model for managing ports
  """
  __slots__ = ('_path_helper', '_extmethods', '__ports',)

  _yang_name = 'demo-port'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ports = YANGDynClass(base=yc_ports_demo_port__ports, is_container='container', yang_name="ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return []

  def _get_ports(self):
    """
    Getter method for ports, mapped from YANG variable /ports (container)

    YANG Description: The root container for port configuration and state
    """
    return self.__ports
      
  def _set_ports(self, v, load=False):
    """
    Setter method for ports, mapped from YANG variable /ports (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ports is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ports() directly.

    YANG Description: The root container for port configuration and state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_ports_demo_port__ports, is_container='container', yang_name="ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ports must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_ports_demo_port__ports, is_container='container', yang_name="ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)""",
        })

    self.__ports = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ports(self):
    self.__ports = YANGDynClass(base=yc_ports_demo_port__ports, is_container='container', yang_name="ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://opennetworking.org/yang/demo', defining_module='demo-port', yang_type='container', is_config=True)

  ports = __builtin__.property(_get_ports, _set_ports)


  _pyangbind_elements = OrderedDict([('ports', ports), ])


