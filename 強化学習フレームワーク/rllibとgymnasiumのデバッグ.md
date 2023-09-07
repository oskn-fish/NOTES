Traceback (most recent call last):
  File "/Users/chinen/Development/Research/esc_mcts/.venv/lib/python3.11/site-packages/tree/__init__.py", line 284, in assert_same_structure
    _tree.assert_same_structure(a, b, check_types)
ValueError: The two structures don't have the same nested structure.

First structure: type=dict str={'obs': (0.9166666666666666, 0.08333333333333333, array([0]), array([0])), 'action_mask': array([1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])}

Second structure: type=OrderedDict str=OrderedDict([('action_mask', array([1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0], dtype=int8)), ('obs', (array([0.49447188, 0.7455682 ], dtype=float32), (1, 0, 3), (2, 3)))])

More specifically: Substructure "type=tuple str=(1, 0, 3)" is a sequence, while substructure "type=float str=0.08333333333333333" is not

