import sys

sys.path.append("../")
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from src.simulators import PnCSimulator
from src.simulators import MenuSimulator

# menu = MenuSimulator()
# param_sampled, outputs = menu.simulate(
#     n_param=1,
#     sim_per_param=1000,
# )
# print("param_sampled: ", param_sampled)
# print("outputs: ", outputs)

pnc = PnCSimulator()
lognorm_params, stat, trajs = pnc.simulate(
    n_param=1,
    sim_per_param=1,
)
# print("stat", stat)
# print("traj", trajs)

df = pd.DataFrame(trajs[0], columns=["k", "pointer_x", "pointer_y", "ball_x", "ball_y"])

sns.scatterplot(x="ball_x", y="ball_y", data=df, color="blue", label="Ball")
sns.scatterplot(x="pointer_x", y="pointer_y", data=df, color="red", label="Pointer")

plt.show()
