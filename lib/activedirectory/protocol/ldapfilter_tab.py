from __future__ import absolute_import
from six.moves import zip

# ldapfilter_tab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '4F128CEA6E6C348C5E33FD02565B75DC'
    
_lr_action_items = {'AND':([2,],[4,]),'APPROX':([5,],[14,]),'RPAREN':([3,7,9,10,11,12,13,18,19,20,21,22,23,24,25,26,27,28,],[11,20,22,23,-1,-5,-8,-14,-6,-4,-7,-3,-2,-9,-13,-12,-10,-11,]),'STRING':([2,14,15,16,17,],[5,25,26,27,28,]),'LTE':([5,],[17,]),'GTE':([5,],[15,]),'EQUALS':([5,],[16,]),'LPAREN':([0,4,6,8,11,13,20,22,23,],[2,2,2,2,-1,2,-4,-3,-2,]),'NOT':([2,],[8,]),'OR':([2,],[6,]),'PRESENT':([5,],[18,]),'$end':([1,11,20,22,23,],[0,-1,-4,-3,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'and':([2,],[3,]),'filterlist':([4,6,13,],[12,19,24,]),'filter':([0,4,6,8,13,],[1,13,13,21,13,]),'item':([2,],[7,]),'not':([2,],[9,]),'or':([2,],[10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> filter","S'",1,None,None,None),
  ('filter -> LPAREN and RPAREN','filter',3,'p_filter','ldapfilter.py',108),
  ('filter -> LPAREN or RPAREN','filter',3,'p_filter','ldapfilter.py',109),
  ('filter -> LPAREN not RPAREN','filter',3,'p_filter','ldapfilter.py',110),
  ('filter -> LPAREN item RPAREN','filter',3,'p_filter','ldapfilter.py',111),
  ('and -> AND filterlist','and',2,'p_and','ldapfilter.py',116),
  ('or -> OR filterlist','or',2,'p_or','ldapfilter.py',120),
  ('not -> NOT filter','not',2,'p_not','ldapfilter.py',124),
  ('filterlist -> filter','filterlist',1,'p_filterlist','ldapfilter.py',128),
  ('filterlist -> filter filterlist','filterlist',2,'p_filterlist','ldapfilter.py',129),
  ('item -> STRING EQUALS STRING','item',3,'p_item','ldapfilter.py',137),
  ('item -> STRING LTE STRING','item',3,'p_item','ldapfilter.py',138),
  ('item -> STRING GTE STRING','item',3,'p_item','ldapfilter.py',139),
  ('item -> STRING APPROX STRING','item',3,'p_item','ldapfilter.py',140),
  ('item -> STRING PRESENT','item',2,'p_item','ldapfilter.py',141),
]
