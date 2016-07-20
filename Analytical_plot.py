import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import brewer2mpl as brew
import math

###############################################
def setupMatplotlib(height=8., width=6.):
    set1 = brew.get_map('Set1', 'Qualitative', 8).mpl_colors
    dark = brew.get_map('Dark2', 'Qualitative', 8).mpl_colors
    paired = brew.get_map('Paired', 'Qualitative', 12).mpl_colors
    reds = brew.get_map('Reds', 'Sequential', 8).mpl_colors
    blues = brew.get_map('Blues', 'Sequential', 9, reverse='True').mpl_colors
    spec = brew.get_map('Spectral', 'Diverging', 8).mpl_colors
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['lines.linewidth'] = 2.0
    plt.rcParams['lines.color'] = 'black'
    plt.rcParams['legend.frameon'] = True
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['legend.fontsize'] = 8
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.color_cycle'] = set1
    # For ipython notebook display set default values.
    # plt.rcParams['lines.markersize'] = 12
    plt.rcParams['figure.figsize'] = (height, width)
    plt.rcParams['grid.linewidth'] = 1

    # General settings used by display and print contexts.
    plt.rcParams['axes.axisbelow'] = True
    grid_line_color = '0.5'
    plt.rcParams['grid.color'] = grid_line_color
    plt.rcParams['grid.linestyle'] = '-'


###############################################
def commonFormat(ax_el: object, centerx: object = None, centery: object = None) -> object:
    # ax_el.set_xlim(0,0.08)
    # ax_el.grid(True)
    # nur einfache Achsen, kein Rahmen
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
    # box = ax_el.get_position()
    # ax_el.set_position([box.x0, box.y0 + box.height * 0.15, box.width, box.height * 0.9])
    # Put a legend below current axis
    # ax_el.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)


############################################
def plot_temp_ana(name):
    #parameters
    rho = 2500  # density
    Cp = 1000   # heat capacity
    mu = 3.2    # thermal conductivity
    alpha = mu/Cp/rho
    T0 = 1  # inital temperature
    t1 = 5.07812e6 # 2months
    t2 = 3.16406e7 # 1year
    t3 = 6.32812e7 # 2years
    t4 = 1.26172e8 # 4years
    # Calculation
    x = np.arange(1, 61)
    T2months = np.zeros(60)
    T1year = np.zeros(60)
    T2years = np.zeros(60)
    T4years = np.zeros(60)
    for i in range(1, 60):
        T2months[i] = T0 * math.erfc(x[i] / math.sqrt(4 * alpha * t1))
        T1year[i] = T0 * math.erfc(x[i] / math.sqrt(4 * alpha * t2))
        T2years[i] = T0 * math.erfc(x[i] / math.sqrt(4 * alpha * t3))
        T4years[i] = T0 * math.erfc(x[i] / math.sqrt(4 * alpha * t4))
    # initiate the first value
    T2months[0] = 1
    T1year[0] = 1
    T2years[0] = 1
    T4years[0] = 1
    # Relative error
    R1 = math.fabs(data2_2m - T2months) / T2months
    R2 = math.fabs(data2_1y - T1year) / T1year
    R3 = math.fabs(data2_2y - T2years) / T2years
    R4 = math.fabs(data2_4y - T4years) / T4years

    setupMatplotlib()
    plt.close('all')
    #fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
    # ax.plot(r, s_tt, label='analytical')
    fig = plt.figure(figsize=(6, 4))
    sub1 = fig.add_subplot(221)
    sub1.set_title('2 months')
    sub1.plot(data1_2m.arc_length, data1_2m.TEMPERATURE1,"b", label='ogs5')
    sub1.plot(data2_2m.arc_length, data2_2m.temperature, "o", mec = "red", mfc ="none", label='ogs6')
    sub1.plot(x, T2months, "g--")
    sub2 = fig.add_subplot(222)
    sub2.set_title('1 year')
    sub2.plot(data1_1y.arc_length, data1_1y.TEMPERATURE1,"b", label='ogs5')
    sub2.plot(data2_1y.arc_length, data2_1y.temperature, "o", mec = "red", mfc ="none", label='ogs6')
    sub2.plot(x, T1year, "g--")
    sub3 = fig.add_subplot(223)
    sub3.set_title('2 years')
    sub3.plot(data1_2y.arc_length, data1_2y.TEMPERATURE1,"b", label='ogs5')
    sub3.plot(data2_2y.arc_length, data2_2y.temperature, "o", mec = "red", mfc ="none", label='ogs6')
    sub3.plot(x, T2years, "g--")
    sub4 = fig.add_subplot(224)
    sub4.set_title('4 years')
    sub4.plot(data1_4y.arc_length, data1_4y.TEMPERATURE1,"b", label='ogs5')
    sub4.plot(data2_4y.arc_length, data2_4y.temperature, "o", mec = "red", mfc ="none", label='ogs6')
    sub4.plot(x, T4years, "g--")
    #ax1.set_title('2 months')
    #commonFormat(ax)
    #ax.set_xlabel('Distance', fontsize=16)
    # ax.xaxis.set_label_coords(0.5,-0.05)
    #ax.set_ylabel('Temperature', fontsize=18)
    #ax.set_xlim(right=10)
    # ax.set_ylim(bottom=3.e-2)
    # ax.set_ylim(top = 7.e-2)
    # ax.set_yscale('log')
    # ax.legend(loc='lower right')
    # ax.yaxis.set_label_coords(-0.05, 0.5)
    fig.tight_layout()
    fig.savefig(name)
    return None


print("The file result_OGS.csv is created by exporting the time series data of one of the upper nodes in the simple heat transport from paraview.")

data1_1y = pd.read_csv('result_OGS5.csv')
data2_1y = pd.read_csv('result_OGS6.csv')
data1_2m = pd.read_csv('result_OGS5_2months.csv')
data2_2m = pd.read_csv('result_OGS6_2months.csv')
data1_2y = pd.read_csv('result_OGS5_2years.csv')
data2_2y = pd.read_csv('result_OGS6_2years.csv')
data1_4y = pd.read_csv('result_OGS5_4years.csv')
data2_4y = pd.read_csv('result_OGS6_4years.csv')

plot_temp_ana('validation.pdf')