import torch
from transformers import pipeline
from transformers import AutoModelForCausalLM, AutoTokenizer
# from dolly.instruct_pipeline import InstructionTextGenerationPipeline

print("load the databricks/dolly-v2-12b")
tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-12b", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-12b", torch_dtype=torch.bfloat16, device_map="auto")
model.save_pretrained("./model")

#generate_text = pipeline(model="databricks/dolly-v2-12b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")
# generate_text("Explain to me the difference between nuclear fission and fusion.")
# generate_text = InstructionTextGenerationPipeline(model=model, tokenizer=tokenizer)
# generate_text("Explain to me the difference between nuclear fission and fusion.")