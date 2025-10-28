# Cloud GPU Inference Instructions

## Setup on Cloud GPU

1. **Activate the virtual environment:**
```bash
source venv/bin/activate
```

2. **Verify GPU availability:**
```bash
python -c "import torch; print('CUDA available:', torch.cuda.is_available())"
```

---

## Test Configuration 1: Matched Duration (22 seconds)
**Video**: sun.mp4 (22 seconds)
**Audio**: input_audio_22sec.wav (22 seconds)

```bash
python -m scripts.inference \
  --inference_config configs/inference/sun_inference_22sec.yaml \
  --unet_config ./models/musetalkV15/musetalk.json \
  --result_dir results \
  --version v15 \
  --use_float16
```

**Output**: `results/v15/sun_input_audio_22sec.mp4`

---

## Test Configuration 2: Full Audio (240 seconds)
**Video**: sun.mp4 (22 seconds - will loop/extend)
**Audio**: input_audio.wav (240 seconds)

```bash
python -m scripts.inference \
  --inference_config configs/inference/sun_inference_full.yaml \
  --unet_config ./models/musetalkV15/musetalk.json \
  --result_dir results \
  --version v15 \
  --use_float16
```

**Output**: `results/v15/sun_input_audio.mp4`

**Note**: This will generate ~6000 frames (240 sec × 25 fps) by cycling through the 22-second source video.

---

## Expected Performance on GPU

- **With CUDA GPU**: ~5-15 frames/second (much faster than MPS)
- **Config 1 runtime**: ~1-2 minutes
- **Config 2 runtime**: ~10-15 minutes

---

## Troubleshooting

If you get "CUDA out of memory" errors, reduce batch size:
```bash
python -m scripts.inference \
  --inference_config configs/inference/sun_inference_22sec.yaml \
  --unet_config ./models/musetalkV15/musetalk.json \
  --result_dir results \
  --version v15 \
  --use_float16 \
  --batch_size 4
```

---

## Download Results

After inference completes, download the output videos:
```bash
# For Config 1
scp user@cloudgpu:~/musetalk/results/v15/sun_input_audio_22sec.mp4 ./

# For Config 2
scp user@cloudgpu:~/musetalk/results/v15/sun_input_audio.mp4 ./
```
