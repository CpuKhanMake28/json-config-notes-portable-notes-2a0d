#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration and runtime parameters for JSON_Config_Notes.
"""

import os
import sys

# Project metadata
PROJECT_NAME = "JSON_Config_Notes"
VERSION = "2.4.1"
BUILD_TAG = "be155368"
DEBUG = False

# Runtime Options
RUNTIME_SETTINGS = {
    "auto_initialize": True,
    "check_updates": True,
    "smooth_tracking": True,
    "adaptive_rate": 60,
    "fov_radius": 110,
    "sensitivity": 2.04,
    "team_check": True,
    "visibility_verification": True,
    "hotkey_trigger": "MouseButton2",
    "theme": "dark_modern",
}

def get_setting(key: str, default=None):
    """Retrieve setting value with fallback."""
    return RUNTIME_SETTINGS.get(key, default)
