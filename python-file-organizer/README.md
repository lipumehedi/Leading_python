
# Python File Organizer

Organize files into folders based on their extensions.

## Features
- Group files by type
- Preview changes with dry-run
- Skip filename conflicts
- Support common image, document, audio and video formats

## Preview first
```bash
python main.py "./test-files" --dry-run
```

## Organize
```bash
python main.py "./test-files"
```

## Safety
Test on a temporary folder first.
Back up important files before organizing them.

## Concepts
pathlib, shutil, dictionaries, argparse and exceptions.
