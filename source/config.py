import torch
import numpy as np

EPOCHS = 1000
BATCH_SIZE = 6 #16
LEARNING_RATE = 2 * 1e-4
NUM_BLOCKS = 30 #36
RES_CHANNELS = 64 #256
TIMESTEP_LAYER_WIDTH = 512 #512
TIME_STEPS = 50
VARIANCE_SCHEDULE = torch.linspace(1e-4, 0.05, TIME_STEPS) #torch.linspace(10e-4, 0.05, TIME_STEPS)
SAMPLE_RATE = 22050 #16000 #22050 #44100
SAMPLE_LENGTH_SECONDS = 5
MAX_SAMPLES = 9000 #9000 # Use "None" for all samples in data input folder; 1000 = ~1h 6min
WITH_CONDITIONING=True

#CONFIG DATA PREP TRANSFORM TO MEL SPECTROGRAM
WINDOW_LENGTH=1024
HOP_LENGTH=256
N_FFT=1024
N_MELS=80
FMIN=20.0
FMAX=SAMPLE_RATE/2
POWER=1.0
NORMALIZED=True