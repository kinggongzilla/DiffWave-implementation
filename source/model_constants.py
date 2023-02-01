import torch

# params used in DiffWave paper for unconditional training in comments below
EPOCHS = 5
BATCH_SIZE = 4 #16
LEARNING_RATE = 2 * 1e-4
NUM_BLOCKS = 5 #36
RES_CHANNELS = 32 #256
TIME_STEPS = 50 #200
VARIANCE_SCHEDULE = torch.linspace(10e-4, 0.02, TIME_STEPS)
LAYER_WIDTH = 128 #512