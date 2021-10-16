#!/usr/bin/env bash

set -ex

python3 ci/macos_app_cleaner.py
cp dist/Test.app/Contents/Resources/qt.conf dist/Test.app/Contents/MacOS/
