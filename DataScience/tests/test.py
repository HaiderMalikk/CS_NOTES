from diffusers import DiffusionPipeline
import torch

# Use a valid model from Hugging Face
pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")

# Move to MPS (Apple GPU) if available
device = "mps" if torch.backends.mps.is_available() else "cpu"
pipe.to(device)

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]

# Show or save the image
image.show()  # or image.save("output.png")
