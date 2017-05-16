# Minor Classes

class Province(object):
	def __init__ (self, name, _type, _quality):
		self.name = name
		self.resource = _type
		self.development_level = 0
		self.worked = False
		self.quality = _quality
		#self.desirability =_desirability

class Colony(object):
    def __init__(self, _name, _resource, _quality):
        self.name = _name
        self.owner = "none"
        self.resource = _resource
        self.development_level = 0
        self.worked = True
        self.quality = _quality


class Minor(object):
    def __init__ (self, _name, _resource, _quality):
        self.name = _name
        self.owner = "none"
        self.resoruce = _resource
        self.development = 0
        self.worked = True
        self.quality = _quality

class Railroad(object):
	def __init__(self, powered, level):
		self.powered = False
		self.level = 0
