# MoMMI - Discord Bot for /vg/station13

MoMMI is a versatile bot designed for the official [/vg/station13 Discord server](http://ss13.moe/). It operates in two distinct parts: a Python component and a Rust component.

## Components

### Python Part

- MoMMI's Python part runs on Python 3.6 (via venv) and consists of multiple modules, each configured through specific configuration files.

### Rust Part

- MoMMI's Rust component runs on Rustc 1.75.0-nightly (cae0791da as of 2023-10-05). It is a Rocket web server responsible for handling potential webhooks (if configured for GitHub) and Byond nudges (world.export).

## Configuration

The configuration files for this project were initially empty. This repository aims to provide clarity on how to configure and use MoMMI.

## Prerequisites

To successfully use the DM compiler, you need to have the Byond DreamMaker command installed on your computer.

## Functionality

### Working Features

MoMMI currently supports the following features:

- Wiggle/Dance
- SS13 Nudges
- DM Code Compilation
- @mommi status
- @mommi help
- @mommi remind
- WYCI/When You Code It
- "Based" (based on what?)
- @mommi magic8ball
- @mommi pick(x, y)
- Channel Mirror

### Unimplemented Features

The following features are not yet implemented:

- GitHub Testmerge (previously available in another bot)

### Known Issues

Some features might not work as expected:

- @mommi help github (configuration error)
- GitHub/Changelog Webhooks (Rust code; not yet configured)

### Unconfigured and Untested

The IRC feature is currently unconfigured and untested.

Please refer to the relevant documentation or contact the project maintainers for further assistance or to report issues.
