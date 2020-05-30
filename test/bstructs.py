# automatically generated by sgrules.py

from structuple import Structuple

class stat(Structuple):
	_members = ('st_mode', 'st_ino', 'st_dev', 'st_nlink', 'st_uid', 'st_gid', 'st_size', 'st_atime', 'st_mtime', 'st_ctime', 'st_crtime')
	def typegen(self):
		return (None, None, None, None, None, None, None, None, None, None, None)

class BPoint(Structuple):
	_members = ('x', 'y')
	def typegen(self):
		return (None, None)

class rgb_color(Structuple):
	_members = ('red', 'green', 'blue', 'alpha')
	def typegen(self):
		return (None, None, None, None)

class BRect(Structuple):
	_members = ('left', 'top', 'right', 'bottom')
	def typegen(self):
		return (None, None, None, None)

class scroll_bar_info(Structuple):
	_members = ('proportional', 'double_arrows', 'knob', 'min_knob_size')
	def typegen(self):
		return (None, None, None, None)

class font_cache_info(Structuple):
	_members = ('sheared_font_penalty', 'rotated_font_penalty', 'oversize_threshold', 'oversize_penalty', 'cache_size', 'spacing_size_threshold')
	def typegen(self):
		return (None, None, None, None, None, None)

class node_ref(Structuple):
	_members = ('device', 'node')
	def typegen(self):
		return (None, None)

class escapement_delta(Structuple):
	_members = ('nonspace', 'space')
	def typegen(self):
		return (None, None)

class tuned_font_info(Structuple):
	_members = ('size', 'shear', 'rotation', 'flags', 'face')
	def typegen(self):
		return (None, None, None, None, None)

class entry_ref(Structuple):
	_members = ('device', 'directory', 'name')
	def typegen(self):
		return (None, None, None)

class app_info(Structuple):
	_members = ('thread', 'team', 'port', 'flags', 'ref', 'signature')
	def typegen(self):
		return (None, None, None, None, entry_ref, None)

class attr_info(Structuple):
	_members = ('type', 'size')
	def typegen(self):
		return (None, None)

class font_height(Structuple):
	_members = ('ascent', 'descent', 'leading')
	def typegen(self):
		return (None, None, None)
