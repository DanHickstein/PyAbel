# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

transforms = [
  ("basex",         '#880000', {}),
  ("basex(var)",    '#880000', {'mfc': 'w'}),
  ("direct_C",      '#EE0000', {}),
  ("direct_Python", '#EE0000', {'mfc': 'w'}),
  ("hansenlaw",     '#CCAA00', {}),
  ("onion_bordas",  '#00AA00', {}),
  ("onion_peeling", '#00CCFF', {}),
  ("three_point",   '#0000FF', {}),
  ("two_point",     '#CC00FF', {}),
  ("linbasex",      '#AAAAAA', {}),
  ("rbasex",        '#AACC00', {}),
  ("rbasex(None)",  '#AACC00', {'mfc': 'w'}),
]

plt.figure(figsize=(6, 6), frameon=False)

plt.xlabel('Image size ($n$, pixels)')
plt.xscale('log')
plt.xlim(5, 1e5)

plt.ylabel('Transform time (seconds)')
plt.yscale('log')
plt.ylim(1e-6, 9.9e3)  # "9.9" to enable minor tics

plt.grid(which='both', color='#EEEEEE')
plt.grid(which='minor', linewidth=0.5)

plt.tight_layout(pad=0.1)

# cubic guiding line
n, t = np.array([1e2, 1e5]), 1e-12
plt.plot(n, t * n**3, color='#AAAAAA', ls=':')
# its annotation (must be done after all layout for correct rotation)
p = plt.gca().transData.transform(np.array([n, t * n**3]).T)
plt.text(n[0], t * n[0]**3, '\n     (cubic scaling)', color='#AAAAAA',
         va='center', linespacing=2, rotation_mode='anchor',
         rotation=90 - np.degrees(np.arctan2(*(p[1] - p[0]))))

# all timings
for meth, color, pargs in transforms:
    pargs.update(color=color)
    if meth == 'two_point':
        ms = 3
    elif meth == 'three_point':
        ms = 5
    elif meth == 'onion_peeling':
        ms = 7
    else:
        ms = 5

    times = np.loadtxt(meth + '.dat', unpack=True)
    n = times[0]
    t = times[1] * 1e-3  # in ms
    plt.plot(n, t, 'o-', label=meth, ms=ms, **pargs)

plt.legend()

# plt.savefig('transform_time.svg')
# plt.show()
