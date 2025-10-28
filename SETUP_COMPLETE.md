# MuseTalk Setup Complete! ✅

**Setup Date:** October 21, 2025
**Platform:** macOS (Darwin 25.0.0)
**Python:** 3.12.8
**Location:** `/Users/rohitfunde/Documents/GitHub/experiments/musetalk`

---

## Installation Summary

### ✅ Environment Setup
- **PyTorch:** 2.9.0 (with MPS/Metal Performance Shaders support)
- **NumPy:** 1.26.4 (downgraded for compatibility)
- **CUDA:** Not available (macOS - using MPS instead)
- **GPU Acceleration:** ✅ MPS (Metal Performance Shaders) available for Apple Silicon

### ✅ Dependencies Installed
- **Core Libraries:**
  - diffusers 0.30.2
  - accelerate 0.28.0
  - transformers 4.39.2
  - gradio 5.24.0

- **MMLab Packages:**
  - mmengine 0.10.7
  - mmcv 2.2.0
  - mmdet 3.3.0
  - mmpose 1.3.2

- **Media Processing:**
  - opencv-python 4.9.0.80
  - ffmpeg 8.0
  - librosa 0.11.0
  - soundfile 0.12.1

### ✅ Model Weights Downloaded
All required model files (13 files, ~8.5GB total):

- ✅ **MuseTalk v1.0:** musetalk.json, pytorch_model.bin (3.2GB)
- ✅ **MuseTalk v1.5:** musetalk.json, unet.pth (3.2GB)
- ✅ **SD VAE:** config.json, diffusion_pytorch_model.bin (319MB)
- ✅ **Whisper Tiny:** config.json, pytorch_model.bin (144MB), preprocessor_config.json
- ✅ **DWPose:** dw-ll_ucoco_384.pth (388MB)
- ✅ **SyncNet:** latentsync_syncnet.pt (1.4GB)
- ✅ **Face Parse BiSeNet:** 79999_iter.pth (51MB), resnet18-5c106cde.pth (45MB)

---

## Quick Start Guide

### 1. Launch Gradio Demo (Web Interface)
```bash
python app.py --use_float16
```
Then open your browser to `http://localhost:7860`

**Note:** Use `--use_float16` to reduce memory usage and improve performance on macOS.

### 2. Run Inference on Video (MuseTalk v1.5)
```bash
python -m scripts.inference \
  --inference_config configs/inference/test.yaml \
  --result_dir results/test \
  --unet_model_path models/musetalkV15/unet.pth \
  --unet_config models/musetalkV15/musetalk.json \
  --version v15
```

**Before running:** Edit `configs/inference/test.yaml` to set:
- `video_path`: Path to your input video or image
- `audio_path`: Path to your input audio file

### 3. Run Real-time Inference
```bash
python -m scripts.realtime_inference \
  --inference_config configs/inference/realtime.yaml \
  --result_dir results/realtime \
  --unet_model_path models/musetalkV15/unet.pth \
  --unet_config models/musetalkV15/musetalk.json \
  --version v15 \
  --fps 25
```

---

## Performance Notes

### macOS Specific Considerations

**GPU Acceleration:**
- ✅ MPS (Metal Performance Shaders) is available and will be used automatically
- MPS provides GPU acceleration on Apple Silicon Macs (M1/M2/M3)
- Performance will be slower than NVIDIA GPUs but faster than CPU-only

**Expected Performance:**
- **Original spec:** 30fps+ on NVIDIA Tesla V100
- **On Apple Silicon (M1/M2/M3):** ~5-15fps (varies by chip)
- **On Intel Mac (CPU only):** ~1-5fps

**Optimization Tips:**
- Use `--use_float16` flag to reduce memory usage
- Close other applications to free up RAM
- Ensure good cooling (Macs throttle when hot)
- Consider using 25fps input videos (matches training data)

---

## Configuration Files

### Main Configs
- `configs/inference/test.yaml` - Normal inference settings
- `configs/inference/realtime.yaml` - Real-time inference settings
- `configs/training/preprocess.yaml` - Data preprocessing
- `configs/training/stage1.yaml` - Training stage 1
- `configs/training/stage2.yaml` - Training stage 2

### Test Data
Sample videos and audio files are located in:
- `data/video/` - Sample input videos
- `data/audio/` - Sample audio clips

---

## Troubleshooting

### Common Issues

**1. Out of Memory Errors**
```bash
# Use float16 precision
python app.py --use_float16
```

**2. Slow Performance**
- This is expected on macOS without NVIDIA GPU
- Try reducing video resolution
- Use shorter video clips for testing

**3. FFmpeg Not Found**
```bash
# Verify FFmpeg is accessible
ffmpeg -version

# If not found, reinstall
brew install ffmpeg
```

**4. Import Errors**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

---

## Repository Structure

```
musetalk/
├── app.py                  # Gradio web interface
├── train.py               # Training script
├── configs/               # Configuration files
├── data/                  # Sample data
├── models/                # Downloaded model weights
├── musetalk/              # Core library code
├── scripts/               # Inference scripts
│   ├── inference.py       # Normal inference
│   └── realtime_inference.py  # Real-time inference
└── results/               # Output directory (created automatically)
```

---

## Next Steps

### To Fork This Repository

1. Go to https://github.com/TMElyralab/MuseTalk
2. Click "Fork" button
3. Update your local clone:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/MuseTalk.git
git push
```

### To Train Your Own Model

See the training documentation in the README.md

### To Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request to the original repository

---

## Resources

- **Original Repository:** https://github.com/TMElyralab/MuseTalk
- **HuggingFace:** https://huggingface.co/TMElyralab/MuseTalk
- **Demo Space:** https://huggingface.co/spaces/TMElyralab/MuseTalk
- **Technical Report:** https://arxiv.org/abs/2410.10122

---

## Support

If you encounter issues:
1. Check the original repository's Issues page
2. Refer to the detailed README.md in this directory
3. Check the requirements match your system

---

**Happy lip-syncing!** 🎤✨
