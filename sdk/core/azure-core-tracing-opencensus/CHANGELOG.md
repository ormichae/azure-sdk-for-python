
# Release History

## 1.0.0b8 (Unreleased)

- Fix for supporting `kind` keyword while instantiating the span.

## 1.0.0b7 (2021-04-08)

- `Link` and `SpanKind` can now be added while creating the span instance.

## 1.0.0b6 (2020-05-04)

- `link` and `link_from_headers` now accept attributes.

## 1.0.0b5 (2019-01-14)

### Bugfix

- Fix context passing for multi-threading
- Don't fail on unknown span type, but maps to PRODUCER or UNSPECIFIED

### Features

- Implement new "change_context" API

## 1.0.0b4 (2019-10-07)

### Features

- Opencensus implementation of azure-core tracing protocol
