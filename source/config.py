import torch

#CONFIG TRAINING AND SAMPLING
EPOCHS = 2000
BATCH_SIZE = 8
PRED_NOISE=True
LEARNING_RATE = 2 * 1e-4
TIME_STEPS = 100 if not PRED_NOISE else 100
FIXED_TIMESTEPS = True #i think has to be true when using DiffWave model
VARIANCE_SCHEDULE = torch.linspace(1e-5, 1, TIME_STEPS)
WITH_CONDITIONING=True
NOISE_SCHEDULE_FUNC = 'cos' # 'exp'  'cos'  'linear'
TAU = 0.5
WITH_DROPOUT = False
SCALE = 1
SAMPLING_ALGORITHM = 'DDIM' # 'DDIM' or 'DDPM'
NUM_BLOCKS = 30 #36
RES_CHANNELS = 256 #256
TIMESTEP_LAYER_WIDTH = 512 #512


#CONFIG DATA PREP 
MAX_SAMPLES = 2200 #9000 # Use "None" for all samples in data input folder
MAX_SAMPLES_VALIDATION = 1000
SAMPLE_RATE = 44100 #16000 #22050 #44100
WINDOW_LENGTH=1024
HOP_LENGTH=256
N_FFT=1024
N_MELS=128
FMIN=20.0
FMAX=SAMPLE_RATE/2
POWER=1.0
NORMALIZED=True
SAMPLE_LENGTH_SECONDS = 5
