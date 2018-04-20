
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AND ASSIGN BOOL COLON COMMA CONST CTMC DIV DOUBLE DTMC ENDMODULE EQ FALSE FORMULA GE GLOBAL GT INIT INT LABEL LB LE LP LT MINUS MODELTYPE MODULE MUL NAME NEQ NOT NUM NUMBERSIGN OR QUOTE RB RP SEMICOLON THEN TRUE TYPEbool_expr : bool_expr AND bool_expr_unitbool_expr : bool_expr OR bool_expr_unitbool_expr : bool_expr_unitbool_expr_unit : NAME EQ NUM\n                      | NAME NEQ NUM\n                      | NAME GT NUM\n                      | NAME LT NUM\n                      | NAME GE NUM\n                      | NAME LE NUM'
    
_lr_action_items = {'AND':([2,3,12,13,14,15,16,17,18,19,],[10,-3,-9,-6,-8,-7,-4,-5,-1,-2,]),'GT':([1,],[5,]),'NAME':([0,10,11,],[1,1,1,]),'LT':([1,],[7,]),'GE':([1,],[6,]),'LE':([1,],[4,]),'NUM':([4,5,6,7,8,9,],[12,13,14,15,16,17,]),'$end':([2,3,12,13,14,15,16,17,18,19,],[0,-3,-9,-6,-8,-7,-4,-5,-1,-2,]),'EQ':([1,],[8,]),'OR':([2,3,12,13,14,15,16,17,18,19,],[11,-3,-9,-6,-8,-7,-4,-5,-1,-2,]),'NEQ':([1,],[9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'bool_expr':([0,],[2,]),'bool_expr_unit':([0,10,11,],[3,18,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> bool_expr","S'",1,None,None,None),
  ('bool_expr -> bool_expr AND bool_expr_unit','bool_expr',3,'p_bool_expr','boolexprtest.py',15),
  ('bool_expr -> bool_expr OR bool_expr_unit','bool_expr',3,'p_bool_expr2','boolexprtest.py',23),
  ('bool_expr -> bool_expr_unit','bool_expr',1,'p_bool_expr3','boolexprtest.py',31),
  ('bool_expr_unit -> NAME EQ NUM','bool_expr_unit',3,'p_bool_expr_unit','boolexprtest.py',36),
  ('bool_expr_unit -> NAME NEQ NUM','bool_expr_unit',3,'p_bool_expr_unit','boolexprtest.py',37),
  ('bool_expr_unit -> NAME GT NUM','bool_expr_unit',3,'p_bool_expr_unit','boolexprtest.py',38),
  ('bool_expr_unit -> NAME LT NUM','bool_expr_unit',3,'p_bool_expr_unit','boolexprtest.py',39),
  ('bool_expr_unit -> NAME GE NUM','bool_expr_unit',3,'p_bool_expr_unit','boolexprtest.py',40),
  ('bool_expr_unit -> NAME LE NUM','bool_expr_unit',3,'p_bool_expr_unit','boolexprtest.py',41),
]
