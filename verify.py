###############################################
def setupMatplotlib(height=8.,width=6.):
        set1=brew.get_map('Set1','Qualitative',8).mpl_colors
        dark=brew.get_map('Dark2','Qualitative',8).mpl_colors
        paired=brew.get_map('Paired','Qualitative',12).mpl_colors
        reds=brew.get_map('Reds','Sequential',8).mpl_colors
        blues=brew.get_map('Blues','Sequential',9,reverse='True').mpl_colors
        spec=brew.get_map('Spectral','Diverging',8).mpl_colors
        plt.rcParams['xtick.direction']='out'
        plt.rcParams['ytick.direction']='out'
        plt.rcParams['lines.linewidth']= 2.0
        plt.rcParams['lines.color']= 'black'
        plt.rcParams['legend.frameon']=True
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['legend.fontsize']=8
        plt.rcParams['font.size'] = 12
        plt.rcParams['axes.color_cycle']=set1
        # For ipython notebook display set default values.
        #plt.rcParams['lines.markersize'] = 12
        plt.rcParams['figure.figsize'] = (height,width)
        plt.rcParams['grid.linewidth'] = 1

        # General settings used by display and print contexts.
        plt.rcParams['axes.axisbelow'] = True
        grid_line_color = '0.5'
        plt.rcParams['grid.color'] = grid_line_color
        plt.rcParams['grid.linestyle'] = '-'

###############################################
def commonFormat(ax_el,centerx=None,centery=None):
        #ax_el.set_xlim(0,0.08)
        #ax_el.grid(True)
        #nur einfache Achsen, kein Rahmen
        ax_el.spines['top'].set_visible(0)
        ax_el.spines['right'].set_visible(0)
        ax_el.spines['bottom'].set_linewidth(0.5)
        ax_el.spines['left'].set_linewidth(0.5)
        ax_el.xaxis.set_ticks_position('bottom')
        ax_el.yaxis.set_ticks_position('left')
        if ((centerx is not None) and (centery is not None)):
                ax_el.spines['left'].set_position(('data', centerx))
                ax_el.spines['bottom'].set_position(('data', centery))
                ax_el.spines['right'].set_position(('data', centerx - 1))
                ax_el.spines['top'].set_position(('data', centery - 1))
        # Shink current axis's height by 10% on the bottom
        ax_el.legend(loc='upper right')
        #box = ax_el.get_position()
        #ax_el.set_position([box.x0, box.y0 + box.height * 0.15, box.width, box.height * 0.9])
        # Put a legend below current axis
        #ax_el.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)

def plot_stress_el(name):
        #parameters
        s0 = 0.01
        a = 2.
        r = np.arange(2.,10.2,0.2)
        theta = 90.*np.pi/180.
        #stress
        s_rr = s0/2. * ((1 - a**2./r**2.) + (1 + 3.*a**4./r**4. - 4.*a**2./r**2.) * np.cos(2.*theta))
        s_tt = s0/2. * ((1 + a**2./r**2.) - (1 + 3.*a**4./r**4.) * np.cos(2.*theta))
        s_rt = - s0/2. * ((1 - 3.*a**4./r**4. + 2.*a**2./r**2.) * np.sin(2.*theta))
        setupMatplotlib()
        plt.close('all')
        #plt.rcParams['legend.fontsize']=14
        #plt.rcParams['font.size'] = 14
        fig, ax = plt.subplots(nrows=1,ncols=1)
        #ax.plot(r,s_rr,label='analytical')
        ax.plot(r,s_tt,label='analytical')
        ax.plot(data.arc_length+2.,data.sigma_yy,label='ogs6')
        #ax.plot(data.Time,data.STRAIN_XY*50.,label='numerical',ls='--',lw=4.)
        commonFormat(ax)
        ax.set_xlabel('$r$', fontsize=16)
        #ax.xaxis.set_label_coords(0.5,-0.05)
        ax.set_ylabel('$\\sigma_\\mathrm{\phi \phi}$', fontsize=18)
        ax.set_xlim(right=10)
        #ax.set_ylim(bottom=3.e-2)
        #ax.set_ylim(top = 7.e-2)
        #ax.set_yscale('log')
        #ax.legend(loc='lower right')
        #ax.yaxis.set_label_coords(-0.05, 0.5)
        fig.tight_layout()
        fig.savefig(name)
        return None

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import brewer2mpl as brew

print("The file result0.csv is created by exporting the time series data of one of the upper nodes in the simple shear test from paraview.")

data = pd.read_csv('result0.csv')

plot_stress_el('validation.pdf')

