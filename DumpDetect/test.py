import torch

# Check if CUDA is available
if torch.cuda.is_available():
    # Set device to GPU
    device = torch.device("cuda")
    print("CUDA is available. Using GPU.")
else:
    # Set device to CPU
    device = torch.device("cpu")
    print("CUDA is not available. Using CPU.")

# Now you can use this device with your PyTorch tensors and models
# For example:
tensor = torch.tensor([1, 2, 3], device=device)