"""Comparison for one fixed wave; all-wave threshold shown as a lower bound."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from check import energy, models
a=np.linspace(0,.30,61)
fig,ax=plt.subplots(figsize=(7.4,4.35),layout='constrained')
for model,label,color in [(models.zeta(),'Riemann ζ','#176682'),(models.fth(.25),'Shifted control, θ = ¼','#b23d2b')]:
    ax.plot(a,[energy(model,x) for x in a],label=label,color=color,lw=2.4)
ax.axhline(0,color='#494949',lw=.8)
ax.axvline(.25,color='#777777',lw=1,ls=':')
ax.annotate('All-wave threshold for the control ≥ ¼',(.25,-.65),(.133,-.7),
            fontsize=9,arrowprops={'arrowstyle':'->','color':'#555555'})
ax.scatter([.0933885065],[0],s=26,color='#b23d2b',zorder=3)
ax.annotate('Wave crosses zero at 0.09339',(.0933885065,0),(.107,-.25),
            fontsize=9,arrowprops={'arrowstyle':'->','color':'#555555'})
ax.set(xlabel='Damping a',ylabel='Completed Weil pairing for the fixed wave',
       title='Damping can hide an off-line pair',xlim=(0,.30))
ax.legend(frameon=False,loc='upper left')
ax.spines[['top','right']].set_visible(False)
fig.savefig('damping.png',dpi=200)
