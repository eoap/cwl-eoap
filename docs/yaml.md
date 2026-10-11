# YAML: a one-minute reference

CWL packages and job files in this module use YAML. You only need three structures to read the example.

## Values and maps

Write `key: value`, with a space after the colon. Indentation nests values under a parent key; use spaces, not tabs.

```yaml
geotiff:
  value: https://example.org/image.tif
```

Here `geotiff` is a map containing a `value` string. This matches the lesson's URI record input. A bare `geotiff: https://example.org/image.tif` would have a different type.

## Lists

A dash introduces a list item. Brackets are a compact alternative:

```yaml
arguments:
  - bounds
# Equivalent: arguments: [bounds]
```

The package's `$graph` is a list of process descriptions, including the workflow and tool.

## Quotes and comments

Quote values when punctuation or an intended string type could be ambiguous. In particular, quote a fragment such as `'#URI'`: an unquoted `#` following whitespace starts a comment.

```yaml
cwlVersion: v1.2
input_type: '#URI'  # A schema reference represented as a string
version_label: '1.0.0'
```

`true` is a boolean and `42` is a number; `'42'` is a string. Preserve the type expected by the CWL input.

Return to [the example](quick-start.md). See the [YAML specification](https://yaml.org/spec/1.2.2/) for the full syntax.
