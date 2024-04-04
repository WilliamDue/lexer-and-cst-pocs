import matplotlib.pyplot as plt
import numpy as np

# Data
input_sizes = np.array([10485760, 20971520, 31457280, 41943040, 52428800, 62914560, 73400320, 83886080, 94371840, 104857600])
rust_times = np.array([44866, 86898, 131183, 180367, 214258, 274776, 330414, 370787, 430997, 469772])
c_times = np.array([24440, 47876, 70986, 98906, 118350, 148982, 175402, 200867, 234474, 248722])
futhark_times = np.array([3388, 6960, 10667, 14400, 17744, 23108, 26358, 30512, 34591, 39199])

# Convert input sizes from bytes to MiB
input_sizes_mib = input_sizes / (1024*1024)

# Convert time elapsed from microseconds to milliseconds
rust_times_ms = rust_times / 1000
c_times_ms = c_times / 1000
futhark_times_ms = futhark_times / 1000

# Linear regression
rust_slope, rust_intercept = np.polyfit(input_sizes_mib, rust_times_ms, 1)
c_slope, c_intercept = np.polyfit(input_sizes_mib, c_times_ms, 1)
futhark_slope, futhark_intercept = np.polyfit(input_sizes_mib, futhark_times_ms, 1)

# Plot
plt.figure(figsize=(10, 6))
rust_line, = plt.plot(input_sizes_mib, rust_times_ms, marker='o', label='Rust implementation')
c_line, = plt.plot(input_sizes_mib, c_times_ms, marker='o', label='C implementation')
futhark_line, = plt.plot(input_sizes_mib, futhark_times_ms, marker='o', label='Futhark implementation')

# Get colors of the original lines
rust_color = rust_line.get_color()
c_color = c_line.get_color()
futhark_color = futhark_line.get_color()

# Linear regression
rust_slope, rust_intercept = np.polyfit(input_sizes_mib, rust_times_ms, 1)
c_slope, c_intercept = np.polyfit(input_sizes_mib, c_times_ms, 1)
futhark_slope, futhark_intercept = np.polyfit(input_sizes_mib, futhark_times_ms, 1)

# Plot linear fits with the same colors
plt.plot(input_sizes_mib, rust_slope * input_sizes_mib + rust_intercept, '--', color=rust_color, label=f'Rust fit: {rust_slope:.2f}x + {rust_intercept:.2f}')
plt.plot(input_sizes_mib, c_slope * input_sizes_mib + c_intercept, '--', color=c_color, label=f'C fit: {c_slope:.2f}x + {c_intercept:.2f}')
plt.plot(input_sizes_mib, futhark_slope * input_sizes_mib + futhark_intercept, '--', color=futhark_color, label=f'Futhark fit: {futhark_slope:.2f}x + {futhark_intercept:.2f}')


plt.xlabel('Input Size (MiB)')
plt.ylabel('Time elapsed (ms)')
plt.title('Lisp Lexer Benchmarks')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show plot
plt.savefig("plot.png", dpi=200)

