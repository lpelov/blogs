import torch
from transformers import pipeline

print("load the databricks/dolly-v2-12b")
generate_text = pipeline(model="databricks/dolly-v2-12b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")

generate_text("Explain to me the difference between nuclear fission and fusion.")