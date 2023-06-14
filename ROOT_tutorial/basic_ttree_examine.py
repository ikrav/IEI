#
# In this example, we expect that the TTree object named "tree" is already created
# and has the structure as in basic_ttree.py example.
#

from ROOT import TH1F
from ROOT import TH2F

def examine(tree):
    # Print the tree structure
    tree.Print()
    
    # Print a particular event content, #11 in this example
    # Note: arrays are not printed in full, only the beginning is shown
    tree.Show( 11 )
    
    # Print one or several variables 
    # Only first argument is required
    # Second argument: selection criteria if any
    # Third argument: format of printed numbers
    # Fourth argument: how many events to print
    tree.Scan("event_number:event_type","","",15)

    total_events = tree.GetEntries()
    signal_events = tree.GetEntries("event_type == 0")
    print("Total events ", total_events, " of which signal events are ", signal_events)

# Define a function that draws SNR for all events
def draw_SNR(tree):
    
    # Simplest way to draw a variable
    tree.Draw("SNR")

# Set up desired histogram for 1D
hist1 = TH2F("histogram","SNR vs event type",100, 0, 20, 2, -0.5, 1.5)
hist1.GetXaxis().SetTitle("Signal-to-Nose")

# Define the function that draws SNR for signal only events
def draw_signal_SNR(tree):

    # A more complex drawing which includes selection requirements
    # and creates a histogram of desired sort
    
    # Draw from the tree with selection
    tree.Draw("SNR>>histogram","event_type == 0")


# Set up desired histogram for 2D
hist2 = TH2F("histogram2D","SNR vs event type",100, 0, 20, 2, -0.5, 1.5)
hist2.GetXaxis().SetTitle("Signal-to-Nose")
hist2.GetYaxis().SetTitle("Event type (0-signal, 1-background)")

# Define the function that draws SNR for signal only events
def draw_SNR_vs_type(tree):

    # A more complex drawing which includes selection requirements
    # and creates a histogram of desired sort
        
    ## Draw from the tree with selection
    tree.Draw("event_type:SNR>>histogram2D","","colz")
