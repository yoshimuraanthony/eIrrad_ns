from eIrrad.sum import plotSVsEb, plotKCon

"""All plots used for manuscript."""

def plotSVsEb_hBN():
    plotSVsEb(
        mat = 'hBN',
        outfile= 'sVsEb.pdf',
        root1 = '/g/g16/yoshia/radEffects/writeups/eIrrad_ns/plots/',
        root2 = 'Eb',
        ebounds = [0,100],
        pbounds = [0,1],
        )

def plotSVsEb_MoS2():
    plotSVsEb(
        mat = 'MoS2',
        outfile= 'sVsEb.pdf',
        root1 = '/g/g16/yoshia/radEffects/writeups/eIrrad_ns/plots/',
        root2 = 'Eb',
        ebounds = [0,100],
        pbounds = [0,5],
        )



