#!/usr/bin/env python
"""
Wrapper script to run MuseTalk inference with PyTorch 2.6 compatibility patch.
This patches torch.serialization to handle weights_only parameter issues.
"""
import torch
import sys
import warnings

# Comprehensive monkey-patch for PyTorch 2.6 weights_only issue
# We need to patch at the UnpicklerWrapper level
original_unpickler_wrapper_init = torch.serialization.UnpicklerWrapper.__init__

def patched_unpickler_wrapper_init(self, *args, **kwargs):
    # Remove weights_only if it's in kwargs, as UnpicklerWrapper doesn't accept it
    if 'weights_only' in kwargs:
        del kwargs['weights_only']
    return original_unpickler_wrapper_init(self, *args, **kwargs)

torch.serialization.UnpicklerWrapper.__init__ = patched_unpickler_wrapper_init

# Also patch torch.load to default to weights_only=False
original_load = torch.load

def patched_load(f, map_location=None, pickle_module=None, *, weights_only=None, **kwargs):
    # Force weights_only=False if not explicitly set
    if weights_only is None:
        weights_only = False

    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', category=FutureWarning)
        warnings.filterwarnings('ignore', message='.*weights_only.*')
        return original_load(f, map_location=map_location, pickle_module=pickle_module,
                           weights_only=weights_only, **kwargs)

torch.load = patched_load

print("=" * 70)
print("MuseTalk Inference Runner (with PyTorch 2.6 compatibility)")
print("=" * 70)
print("Applied compatibility patches for checkpoint loading")
print()

# Now import and run the inference script
from scripts.inference import main, parser

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
