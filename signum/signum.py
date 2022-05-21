
import numpy as np
import plotly.graph_objects as go    # for data visualisation
import plotly.io as pio              # to set shahin plot layout

def gen_sinewave(freq=100, samp_rate=5000, plot=False, save=False):
    '''
    Generate a sine with a given frequency and sampling rate

    Parameters
    ----------
    freq: int
        sine wave frequency in Hertz
    sampe:rate: int
        sampling rate used to generate the sine wave
    plot: boolean
        if True, plots the geneated sine wave
    save: boolean
        if True, saves the generated sinve wave into a file

    Returns
    -------
    None
    '''
    sample_rate = samp_rate
    frequency   = freq
    amplitude   = 1

    time     = np.arange(0, 0.2, 1/sample_rate);
    sinewave = np.empty(len(time))

    sinewave = amplitude*np.sin(2*np.pi*frequency*time)

    if plot is True:
        fig = go.Figure(layout=dict(xaxis=dict(title='Time (s)'),yaxis=dict(title='Amplitude (V)')))
        fig.add_scatter(x=time, y=sinewave)
        fig.show()

    if save is True:
        pass
