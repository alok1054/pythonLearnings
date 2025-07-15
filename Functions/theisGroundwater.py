import numpy as np
import matplotlib.pyplot as plt
from scipy.special import exp1 as W

def theis(r, t, Q, T, S):
    """Use the Theis equation to get drawdown
    in a confined aquifer at a distance r
    from a well pumping at rate Q, for time t.

    Parameters
    ----------
    r : float or array or floats
        Distance to the pumping well (L)
    t : float or list-like of floats
        Times to calculate drawdown at (T)
    Q : float
        Pumping rate (L3/T)
    T : float
        Aquifer transmissivity (L2/T)
    S : float
        Aquifer storativity

    Returns
    -------
    s : float array
        Drawdown for all values of r or t

    Notes
    -----
    If r is a 1 or 2D array, t must be scalar.
    If t is non-scalar (list-like), r must be scalar.

    Examples
    --------
    #>>> theis(1000, 10, Q=4088, T=1000, S=3e-4)
    array([1.40636669])
    """

    # coerce time input into a numpy array
    # (so that we can use the same code
    #  for vector or scalar inputs of t)
    if np.isscalar(t):
        t = [t]
    t = np.array(t, dtype=float)

    # dimensionless time parameter
    # (only compute for non-zero times)
    u = r**2 * S / (4 * T * t)

    s = Q / (4 * np.pi * T) * W(u)
    return s


theis(1000, 10, Q=4088, T=1000, S=3e-4)

times = np.logspace(-1, 1, 100)
s = theis(1000, times, Q=4088, T=1000, S=3e-4)

plt.plot(times, s)
plt.ylabel('Drawdown, in meters')
plt.xlabel('Time, in days')

def get_distance(x0, y0, x1, y1):
    """Compute the distance between two points.

    Parameters
    ----------
    x0 : float or array-like
        x-coordinate(s) for computing distance
    y0 : float or array-like
        y-coordinate(s) for computing distance
    x1 : float
        x-coordinate to compute distance from
    y1 : float
        y-coordinate to compute distance from

    Returns
    -------
    distance : float or array
        Distance of each point defined by x0, y0 from
        x1, y1.
    """
    return np.sqrt((x1-x0)**2 + (y1-y0)**2)


def theis_xy(x, y, pumping_well_xy, t, Q=1.16, T=100, S=0.0001):
    """Use the Theis equation to get drawdown
    in a confined aquifer at any x, y point(s),
    for a pumping well at (x, y) location pumping_well_xy,
    pumping at rate Q, for time t.

    Parameters
    ----------
    x : float or list-like of floats
        x-coordinates for computing drawdown.
    y : float or list-like of floats
        y-coordinates for computing drawdown.
    pumping_well_xy : tuple
        (x, y) location of the pumping well
    t : float or list-like of floats
        Times to calculate drawdown at (T)
    Q : float
        Pumping rate (L3/T)
    T : float
        Aquifer transmissivity (L2/T)
    S : float
        Aquifer storativity

    Returns
    -------
    s : list of arrays
        Arrays of drawdown (of same shape as x and y),
        at each time in t.
    """
    if np.isscalar(t):
        t = [t]
    if np.isscalar(x):
        x = [x]
    if np.isscalar(y):
        y = [y]
    x = np.array(x)
    y = np.array(y)

    s = []
    for ts in t:
        s_t = []
        r = get_distance(x, y, *pumping_well_xy)
        s_xy = theis(r, t, Q=Q, T=T, S=S)
        s_t.append(s_xy)
        s_t = np.reshape(s_t, np.shape(x))
        s.append(s_t)
    return s

#%%time
x, y = np.meshgrid(np.arange(2000), np.arange(2000))
pumping_well_xy = (1000, 1000)

s = theis_xy(x, y, pumping_well_xy, 10, Q=4088, T=1000, S=3e-4)

theis_xy(1000, 0, (1000, 1000), 10, Q=4088, T=1000, S=3e-4)

plt.imshow(s[0])

s1 = theis_xy(x, y, (1000, 1000), 10, Q=4088, T=1000, S=3e-4)
s2 = theis_xy(x, y, (500, 500), 10, Q=4088, T=1000, S=3e-4)

s_total = s1[0] + s2[0]
fig, ax = plt.subplots(figsize=(10, 10))
im = ax.imshow(s_total)
cs = ax.contour(s_total, colors='w', levels=np.arange(0, 10))
ax.clabel(cs, inline=True, fmt='%.2f', fontsize=10)
fig.colorbar(im, label='Drawdown, in meters', shrink=0.8, pad=0.02)