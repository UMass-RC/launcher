import os

env_vars = ["SLURM_CPUS_ON_NODE","LAUNCHER_CORES_PER_TASK"]
for ev in env_vars:
  print(f"{ev} = {os.getenv(ev)}")
