import matplotlib.pyplot as plt
import numpy as np
import subprocess
try:
    a0 = np.genfromtxt('data_chart\\241230wavelength_chart.csv', delimiter=",", skip_header=1)
except Exception as e:
    print(f"Error loading data: {e}")
    raise
fig, ax = plt.subplots(figsize=(5.5, 3.5))
ax.plot(a0[:, 0] / 1e6, a0[:, 1]*1e2, color="black", lw=1, ls='-', marker='o', markersize=0, label=r'$\varepsilon_r=1$')
ax.plot(a0[:, 0] / 1e6, a0[:, 2]*1e2, color="red", lw=1, ls='-', marker='o', markersize=0, label=r'$\varepsilon_r=2.26$')
ax.plot(a0[:, 0] / 1e6, a0[:, 3]*1e2, color="green", lw=1, ls='-', marker='o', markersize=0, label=r'$\varepsilon_r=4.7$')
ax.plot(a0[:, 0] / 1e6, a0[:, 4]*1e2, color="blue", lw=1, ls='-', marker='o', markersize=0, label=r'$\varepsilon_r=10$')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim([10, 10000])
ax.set_ylim([1, 10000])
ax.set_title(r'Wavelength Chart')
ax.set_xlabel(r'Frequency [MHz]', fontsize=11)
ax.set_ylabel(r'Effective Wavelength $\lambda_{\mathrm{eff}}$ [cm]', fontsize=11)
ax.legend(loc='upper right')
ax.grid(ls=':')
fig.subplots_adjust(left=0.13, right=0.95, bottom=0.15, top=0.92)
PdfFile = 'data_chart\\241230wavelength_chart.pdf'
fig.savefig(PdfFile)
subprocess.Popen(['start', PdfFile], shell=True)