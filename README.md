# DiffWave-implementation
A custom DiffWave implementation for the Practical Work in AI course at JKU. 

# Set up environment with dependencies
1. Load conda env with "conda create -n <environment-name> --file req.txt"
2. Activate conda environment with "conda activate <environment-name>"
3. If on Mac/Linux install sox with "conda install -c conda-forge sox" (a dependency of torchaudio)

# Prepare data
By default, when using source/data_prep.py, full length audio files are chunked into fixed length samples of 4 seconds (length is configurable). Mel spectrograms are computed for each chunked sample.
Default input folder for data processing is "raw_samples"
Default output folder for chunked audio is "data/chunked_audio"
Default output folder for mel spectrograms is "data/mel_spectrograms"

1. Set up a folder "raw_samples" in root directory, containing audio files (.mp3 or .wav) that should be used as training data
2. Make sure that "data/chunked_audio" and "data/mel_spectrograms" folders exist. If not, create them.
3. Run "python data_prep.py" to chop samples in "raw_samples" into 4 second snippets and save to "data/chunked_audio" and spectrograms to "data/mel_spectrograms"
4. Optional: To pass different input/output folders run "python data_prep.py [path to audio_folder] [path to output_folder]"

# How to train a model
All samples used for training have to be of the SAME length and in the same folder (default: "data/chunked_audio")). Samples have to be either .mp3 or .wave .
1. Set desired config parameters in "source/config.py"
2. Run "python source/main.py [path to data_folder] [path to conditional input (i.e. spectrograms)]" to start training. 
Passing [path to data_folder] and [path to conditional input (i.e. spectrograms)] is optional.The default paths are "data/chunked_audio" and "data/mel_spectrograms"

# Note
Sometimes, when using different datasets, the mel spectrograms generated by "source/data_prep.py" have different dimensions. Hence an error in regarding the shape of the ConvTranspose2D layers in SpectrogramConditioner is thrown. To train the model, kernel_size, stride, padding and output_padding of the ConvTranspose2D layers have to be adjusted. Check pytorch docs for more details how to calculate correct parameters: https://pytorch.org/docs/stable/generated/torch.nn.ConvTranspose2d.html