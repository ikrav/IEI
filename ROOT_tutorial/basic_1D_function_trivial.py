from ROOT import TF1

# Define a function setting its name, formula, and range
func = TF1("func", "[0] + [1]*TMath::Exp(-x/[2])", 0, 10)
# This function has parameters [0], [1], and [2], so set them.
func.SetParameter(0, 10)
func.SetParameter(1, 1)
func.SetParameter(2, 2)
# Alternatively one can set all paramneters in one go:
#  func.SetParameters(10,1,2)

# Draw with all the default parameters
func.Draw()

