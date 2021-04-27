# ZypeLang - A OpenSource replacement for JSON

<p align='center'>
    <img height=200 width=200 src='https://raw.githubusercontent.com/Zype-Z/ZypeLang/main/favicon.png'>
</p>

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9fdcf71f2d104721b8bcb1536847c940)](https://app.codacy.com/gh/Zype-Z/ZypeLang?utm_source=github.com&utm_medium=referral&utm_content=Zype-Z/ZypeLang&utm_campaign=Badge_Grade_Settings)
[![Create PyPI Release](https://github.com/Zype-Z/ZypeLang/actions/workflows/ci.yaml/badge.svg)](https://github.com/Zype-Z/ZypeLang/actions/workflows/ci.yaml)

ZypeLang is a OpenSource replacement of JSON based on Python.

## Syntax

```
<key> "value";
```

## How to use it

You can use ZypeLang with **Zype Python SDK**.

### Installation of ZypeSDK for Python

```shell
pip install ZypeSDK # Replace pip with pip3 and/or add sudo according to your Enviroment.
```

### Usage - ZypeSDK for Python

```python3
import ZypeSDK as zype

name = zype.Open("file.zype")['name']

print(name)
```

### Usage ZypeLang
And in `file.zype`

```
<name> "Zype, Inc.";
```

## Why to use

ZypeLang is easier & shorter than JSON

#### Example:

```json
{
    "name": "Rajdeep Malakar"
}
```

To,

```
<name> "Rajdeep Malakar";
```
