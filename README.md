# PyHokchew
A Python library for dealing with Hokchew data.

> This library is currently pre-alpha. Things can change without notice.


## Prerequisite
  - Python 3.6

## Example usage

### Installation
```
pip install git+https://github.com/MindongLab/PyHokchew
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

### 榕拼輸入方案轉手寫方案
```python
>>> from pyhokchew.models.yngping.YngPingTwo import YngPingSyllable
>>> YngPingSyllable.from_string('doeyng55').to_handwritten()
'dëüng'
```

## Developing

### Install from source
> `pip` here refers to PIP 3+

```bash
git clone https://github.com/MindongLab/PyHokchew.git
cd PyHokchew
pip install -e .
```

### Running unit tests
```bash
python -m unittest discover -v . "*Test.py"
```
