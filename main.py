import matplotlib.pyplot as plt
import numpy as np

# Depth array (0 to 10,000 feet)
depth_ft = np.linspace(0, 10000, 500)

# Constants & Gradients
hydrostatic_grad = 0.433  # psi/ft (fresh water base)
mud_weight_ppg = 9.5  # ppg
mud_grad = mud_weight_ppg * 0.052  # psi/ft
obg_grad = 1.00  # psi/ft average overburden gradient

# Pressure calculations
hydrostatic_press = depth_ft * hydrostatic_grad
formation_press = depth_ft * mud_grad
overburden_press = depth_ft * obg_grad

# Plotting profiles
plt.figure(figsize=(8, 10))
plt.plot(hydrostatic_press, depth_ft, label="Hydrostatic Pressure (0.433 psi/ft)", color="blue", linestyle="--")
plt.plot(formation_press, depth_ft, label=f"Formation Pressure ({mud_weight_ppg} ppg mud)", color="green")
plt.plot(overburden_press, depth_ft, label="Overburden Stress (1.00 psi/ft)", color="red")

plt.gca().invert_yaxis()  # Invert axis so depth increases downward
plt.title("Subsurface Pressure vs. Depth Profile")
plt.xlabel("Pressure (psi)")
plt.ylabel("True Vertical Depth (ft)")
plt.grid(True, which="both", linestyle=":", linewidth=0.5)
plt.legend()
plt.tight_layout()

# Save plot output
plt.savefig("pressure_profile.png")
print("Pressure profile plot successfully generated and saved as 'pressure_profile.png'.")
