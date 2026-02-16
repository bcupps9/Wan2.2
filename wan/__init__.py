# Copyright 2024-2025 The Alibaba Wan Team Authors. All rights reserved.
import warnings

from . import configs, distributed, modules
from .image2video import WanI2V
from .text2video import WanT2V

# BEGIN 3dConsistency optional non-I2V/T2V imports
# Keep base I2V/T2V usable even if optional stacks (speech/animate/TI2V deps)
# are missing in this environment.
_OPTIONAL_IMPORT_ERRORS = {}

try:
    from .textimage2video import WanTI2V
except Exception as e:
    WanTI2V = None
    _OPTIONAL_IMPORT_ERRORS["WanTI2V"] = e
    warnings.warn(
        f"[3dConsistency optional import] WanTI2V unavailable: {e}"
    )

try:
    from .animate import WanAnimate
except Exception as e:
    WanAnimate = None
    _OPTIONAL_IMPORT_ERRORS["WanAnimate"] = e
    warnings.warn(
        f"[3dConsistency optional import] WanAnimate unavailable: {e}"
    )

try:
    from .speech2video import WanS2V
except Exception as e:
    WanS2V = None
    _OPTIONAL_IMPORT_ERRORS["WanS2V"] = e
    warnings.warn(
        f"[3dConsistency optional import] WanS2V unavailable: {e}"
    )
# END 3dConsistency optional non-I2V/T2V imports
