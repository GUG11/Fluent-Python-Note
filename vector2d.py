from array import array
import math

class Vector2dV0:
    typecode = 'd'
    
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
        
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) 
                + bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    

class Vector2dV1(Vector2dV0):
    @classmethod
    def frombytes(cls, octets: bytes):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    
    
class Vector2dV2(Vector2dV1):
    def __format__(self, fmt_spec: str=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    
    def angle(self):
        return math.atan2(self.y, self.x)
    
 
class Vector2dV3(Vector2dV2):
    def __init__(self, x: float, y:float):
        self.__x = float(x)
        self.__y = float(y)
        
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    
class Vector2dV3Slots(Vector2dV3):
    __slots__ = ('__x', '__y')