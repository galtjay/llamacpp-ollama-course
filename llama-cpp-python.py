from llama_cpp import Llama

llm = Llama(
      model_path="./models/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf",
      n_gpu_layers=-1, # 取消注释以使用GPU加速
)
output = llm(
      "<｜User｜> 1+1 等于多少？<｜Assistant｜>", # 提示
      max_tokens=512, # 生成最多512个标记，设置为None以生成到上下文窗口的结束
) 

print(output)