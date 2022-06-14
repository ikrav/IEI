import numpy as np
from ROOT import TH1F

xlo = 0
xhi = 50
nbins = 20

binning = np.linspace(xlo, xhi, nbins+1)

hist = TH1F("hist1", "My histogram", nbins, binning)
# Alternatively: hist = TH1F("hist", "My histogram", nbins, xlo, xhi)

# Fill histogram with numbers
hist.Fill(5)
hist.Fill(5)
hist.Fill(9)

# Draw histogram in most basic way
hist.Draw()

# Print histogram content
hist.Print("all")

