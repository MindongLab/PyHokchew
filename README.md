# PyHokchew
A Python library for dealing with Hokchew data.

> This library is currently pre-alpha. Things can change without notice.

## Example usage

### Installation
```
pip install -e git+https://github.com/MindongLab/PyHokchew
```

### Parse Foochow Romanized

```python
>>> from pyhokchew.parser import parse_foochow_romanized as parse
>>> p = parse('cṳ̄ng')
>>> p.get_initial()
'c'
>>> p.get_tone()
2
>>> p.get_final_without_tone()
'ṳng'
>>> p.get_final_with_tone()
'ṳ̄ng'
```

### Convert _Qi Lin Ba Yin (戚林八音)_ Fanqie to Foochow Romanized

```python
>>> from pyhokchew.convert import ciklin_to_foochow_romanized_string as convert
>>> convert('柳','雞','下上')
'liē'
>>> convert('柳','雞','下去')
'liê'
>>> convert('鶯','初','下去')
'âe̤'
>>> convert('鶯','初','下平')
'è̤'
```
