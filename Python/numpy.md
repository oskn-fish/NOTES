# ndarrayの要素抽出はboolのarrayで指定できる
```python
a = np.arange(5)
# a = [0, 1, 2, 3, 4]

bools = [True, False, True, False, False]

a[bools]
# [0, 2, 4]
```