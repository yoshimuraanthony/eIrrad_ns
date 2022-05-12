from dxs.plots import DXSPlot
from dxs.classes import ExciDXS

Ed_dict = {
        'B': 19.36,  # eV (10.1103/PhysRevB.82.113404)
        'N': 23.06,
        'Barm': 12.85,
        'Narm': 12.71,
        }

def plotPristineHBNDXS_240fs(
        save = True,
        outfile = 'pristineHBN.png',
        res = 400,
        T = 1273,  # K
        ):
    """Plots DXS for pristine with tau=240fs, analogous to figure 5."""
    
    # DXS dicts
    BDXS = ExciDXS(spec='B', Ed = Ed_dict['B'], ebounds=[20,100], tau=240,
            res=res, T=T)
    NDXS = ExciDXS(spec='N', Ed = Ed_dict['N'], ebounds=[20,100], tau=240,
            res=res, T=T)
    BarmDXS = ExciDXS(spec='B', Ed = Ed_dict['Barm'], ebounds=[20,100], tau=240,
            res=res, T=T)
    NarmDXS = ExciDXS(spec='N', Ed = Ed_dict['Narm'], ebounds=[20,100], tau=240,
            res=res, T=T)
    B_dict = BDXS.getDict()
    N_dict = NDXS.getDict()
    Barm_dict = BarmDXS.getDict()
    Narm_dict = NarmDXS.getDict()

    # total DXS
    B_ar = B_dict['dxs_ar']
    N_ar = N_dict['dxs_ar']
    Barm_ar = Barm_dict['dxs_ar']
    Narm_ar = Narm_dict['dxs_ar']
    pristot_ar = B_ar + N_ar
    armtot_ar = Barm_ar + Narm_ar
    Eb_ar = Barm_dict['Eb_ar']

    # plot DXS curves
    plot = DXSPlot()
    plot.ax.plot(Eb_ar, armtot_ar, label='edge total', color='black', zorder=2)
    plot.plot(dxs_dict=Barm_dict, color='tab:green', label='edge B')
    plot.plot(dxs_dict=Narm_dict, color='tab:blue', label='edge N')
    plot.ax.plot(Eb_ar, pristot_ar, label='pristine total', color='black',
            linestyle='--', zorder=10)
    plot.plot(dxs_dict=B_dict, color='tab:green', label='pristine B',
            linestyle='--')
    plot.plot(dxs_dict=N_dict, color='tab:blue', label='pristine N',
            linestyle='--')

    # labels and legend
    plot.decorate(title=r'$\tau$ = 240 fs', ylim=(0,60))
    plot.ax.legend(ncol=2)

    if save:
        plot.save(outfile)
    plot.show()


def plotPristineHBNDXSOnly(
        save = True,
        outfile = 'pristineHBN_020ps.png',
        res = 100,
        T = 1273,  # K
        tau = 20000,  # fs
        ):
    """Plots DXS for pristine with tau=240fs, analogous to figure 5."""
    
    # DXS dicts
    BDXS = ExciDXS(spec='B', Ed = Ed_dict['B'], ebounds=[20,100], tau=tau,
            res=res, T=T)
    NDXS = ExciDXS(spec='N', Ed = Ed_dict['N'], ebounds=[20,100], tau=tau,
            res=res, T=T)
    B_dict = BDXS.getDict()
    N_dict = NDXS.getDict()

    # total DXS
    B_ar = B_dict['dxs_ar']
    N_ar = N_dict['dxs_ar']
    pristot_ar = B_ar + N_ar
    Eb_ar = B_dict['Eb_ar']

    # plot DXS curves
    plot = DXSPlot()
    plot.ax.plot(Eb_ar, pristot_ar, label='pristine total', color='black',
            zorder=10)
    plot.plot(dxs_dict=B_dict, color='tab:green', label='pristine B')
    plot.plot(dxs_dict=N_dict, color='tab:blue', label='pristine N')

    # expt data
    plot.ax.plot((30, 60, 60), (21.46, 33.66, 20.44), 's', color='k',
            markersize=7, label='expt')

    # labels and legend
    plot.decorate(title=r'$\tau$ = 20 ps', ylim=(0,100))
    plot.ax.legend()

    if save:
        plot.save(outfile)
    plot.show()
#---------------------------------- SCRATCH -----------------------------------

#     plot.plot(classkey='exci', spec='B', Ed = Ed_dict['Barm'], ebounds=[20,100],
#             tau=240, res=res, T=T, color='tab:green',
#             label='edge B')
#     plot.plot(classkey='exci', spec='N', Ed = Ed_dict['Narm'], ebounds=[20,100],
#             tau=240, res=res, T=T, color='tab:blue',
#             label='edge N')
#     plot.plot(classkey='exci', spec='B', Ed = Ed_dict['B'], ebounds=[20,100],
#             tau=240, res=res, T=T, linestyle='--', color='tab:green',
#             label='pristine B')
#     plot.plot(classkey='exci', spec='N', Ed = Ed_dict['N'], ebounds=[20,100],
#             tau=240, res=res, T=T, linestyle='--', color='tab:blue',
#             label='pristine N')

