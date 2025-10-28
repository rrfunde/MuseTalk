# Running MuseTalk on Google Colab - Step-by-Step Guide

**Time Required:** 15-20 minutes
**Cost:** Free (using free T4 GPU)

---

## Quick Start (3 Steps)

### Step 1: Open Google Colab
1. Go to https://colab.research.google.com/
2. Sign in with your Google account
3. Click **File** → **Upload notebook**
4. Upload the `MuseTalk_Colab_Setup.ipynb` file from this directory

**OR** Create a new notebook and copy-paste the cells

---

### Step 2: Enable GPU
1. Click **Runtime** → **Change runtime type**
2. Under **Hardware accelerator**, select **T4 GPU**
3. Click **Save**

![Enable GPU](https://i.imgur.com/XxXxXxX.png)

---

### Step 3: Run All Cells
1. Click **Runtime** → **Run all**
2. Wait 10-15 minutes for setup to complete
3. Use the Gradio interface that appears

---

## Detailed Instructions

### What Each Section Does

#### 1. **Verify GPU** (Cell 1)
- Checks that GPU is available
- Shows GPU type (T4, V100, etc.)
- Takes: ~5 seconds

#### 2. **Clone Repository** (Cell 2)
- Downloads MuseTalk code from GitHub
- Takes: ~30 seconds

#### 3. **Install Dependencies** (Cells 3-5)
- Installs PyTorch
- Installs Python packages
- Installs MMLab packages (mmcv, mmpose, mmdet)
- Takes: ~5 minutes

#### 4. **Download Models** (Cell 6)
- Downloads ~8.5GB of model weights
- Takes: ~5-10 minutes (depends on connection)

#### 5. **Verify Setup** (Cell 7)
- Checks all models downloaded correctly
- Takes: ~5 seconds

#### 6. **Run MuseTalk** (Choose One)

**Option A: Gradio Web Interface** (Recommended)
- Launches interactive web UI
- Upload videos/audio through browser
- Adjust parameters in real-time
- Get a public shareable link

**Option B: Command-Line**
- Upload files manually
- Run inference via code
- More control over parameters

**Option C: Test with Samples**
- Use built-in test videos
- No upload needed
- Quick test to verify everything works

---

## Using the Gradio Interface

Once you run the Gradio cell, you'll see:

```
Running on public URL: https://xxxxx.gradio.live
```

Click that link to open the interface where you can:

1. **Upload Video:** Click to select your video file
2. **Upload Audio:** Click to select your audio file
3. **Adjust Parameters:**
   - `bbox_shift`: Adjust face region (try -5 to +5)
   - `extra_margin`: Extra space around face
4. **Generate First Frame:** Preview to check alignment
5. **Generate Full Video:** Create the complete lip-synced video

### Tips for Best Results

- **Video:**
  - Use videos with clear, frontal faces
  - 25fps recommended
  - Resolution: 256x256 to 1920x1080

- **Audio:**
  - WAV or MP3 format
  - Clear speech
  - Any language (Chinese, English, Japanese work best)

- **Parameters:**
  - Start with `bbox_shift = 0`
  - If mouth doesn't open enough → increase bbox_shift (+3 to +7)
  - If mouth opens too much → decrease bbox_shift (-3 to -7)

---

## Downloading Your Results

After generation completes:

### Method 1: Through Gradio
- Results appear in the Gradio interface
- Right-click video → Save As

### Method 2: Download from Colab
```python
from google.colab import files
files.download('results/test/output.mp4')
```

### Method 3: Save to Google Drive
```python
from google.colab import drive
drive.mount('/content/drive')

!cp results/test/output.mp4 /content/drive/MyDrive/
```

---

## Performance Expectations

### Free Tier (T4 GPU)
- Processing Speed: ~10-15fps
- 10-second video: ~1-3 minutes
- Memory: 15GB VRAM available
- Limitations: 12-hour session limit

### Colab Pro (Better GPU)
- V100: ~20-30fps
- A100: ~30fps+
- Faster processing
- Longer sessions

---

## Common Issues & Solutions

### 1. "Runtime disconnected"
**Cause:** Idle timeout or out of memory

**Solution:**
```python
# Keep session alive (run in a cell)
import time
while True:
    time.sleep(60)
```

### 2. "Out of memory"
**Solution:**
```python
# Use float16 precision
!python app.py --use_float16

# Or reduce batch size in config
```

### 3. "Cannot download models"
**Solution:**
```python
# Try alternative download
!wget https://huggingface.co/TMElyralab/MuseTalk/resolve/main/musetalkV15/unet.pth -P models/musetalkV15/
```

### 4. "GPU not available"
**Solution:**
- Runtime → Change runtime type → T4 GPU → Save
- Restart runtime
- Run cells again

---

## Advanced Usage

### Process Multiple Videos

```python
videos = ['video1.mp4', 'video2.mp4', 'video3.mp4']
audios = ['audio1.wav', 'audio2.wav', 'audio3.wav']

for i, (video, audio) in enumerate(zip(videos, audios)):
    !python -m scripts.inference \
      --video_path {video} \
      --audio_path {audio} \
      --result_dir results/batch_{i} \
      --unet_model_path models/musetalkV15/unet.pth \
      --unet_config models/musetalkV15/musetalk.json \
      --version v15
```

### Custom Parameters

Edit the config file:
```python
# Modify test.yaml
with open('configs/inference/test.yaml', 'w') as f:
    f.write('''
task_0:
  video_path: "my_video.mp4"
  audio_path: "my_audio.wav"
  bbox_shift: 5
  extra_margin: 10
''')
```

### Save to Google Drive Automatically

```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Set result directory to Drive
!python -m scripts.inference \
  --result_dir /content/drive/MyDrive/MuseTalk_Results \
  ...
```

---

## Cost Breakdown

### Free Tier
- **Cost:** $0
- **GPU:** T4 (16GB)
- **Runtime:** 12 hours/day
- **Storage:** Temporary (deleted after session)

### Colab Pro ($10/month)
- **GPU:** V100 or A100
- **Runtime:** 24 hours
- **Background execution:** Yes
- **Worth it?** If processing many videos

### Colab Pro+ ($50/month)
- **GPU:** A100 priority
- **Runtime:** Longer
- **Resources:** More RAM/disk
- **Worth it?** For production use

---

## Alternatives to Google Colab

If Colab doesn't work or you hit limits:

1. **Kaggle Notebooks** (Free GPU, similar to Colab)
2. **Paperspace Gradient** (Free tier available)
3. **RunPod** (Pay per hour, cheap GPU instances)
4. **AWS SageMaker** (Enterprise, expensive)

---

## Summary

**Pros of Google Colab:**
✅ Free GPU access
✅ No installation needed
✅ Easy to share notebooks
✅ Good for testing/demos
✅ Works from any computer

**Cons:**
❌ 12-hour session limit (free tier)
❌ Can disconnect randomly
❌ Storage not persistent
❌ Slower than local GPU

**Recommendation:** Use Colab for testing and occasional use. For production or frequent use, consider a local GPU setup or cloud GPU rental.

---

## Next Steps

1. **Upload the notebook** to Google Colab
2. **Enable GPU runtime**
3. **Run all cells**
4. **Test with sample data** first
5. **Upload your own videos** and experiment!

Happy lip-syncing! 🎤✨
