import ROOT as r
import sys, os

# r.gStyle.SetOptStat(0)

file = r.TFile (sys.argv[1])
tree = file.Get("hcalTupleTree/tree");
canv = r.TCanvas()

occ_hist = r.TH2F("occ_hist","occ_hist", 83, -41.5, 41.5, 72, 0.5, 72.5 );
occ_hist.GetXaxis().SetTitle("ieta");
occ_hist.GetYaxis().SetTitle("iphi");
occ_hist.SetTitle("HF Digi Occupancy");

size_hist = r.TH1F("size_hist", "size_hist", 100, 0, 2000 );
size_hist.GetXaxis().SetTitle("HF Digi Collection Size");
size_hist.GetYaxis().SetTitle("Number of entries");
size_hist.SetTitle("HF Digi Collection Size");

# tree.Draw("HFDigiIPhi:HFDigiIEta>>occ_hist", "HFDigiDepth == 1")
tree.Draw("HFDigiIPhi:HFDigiIEta>>occ_hist")
occ_hist.Draw("COLZ");
canv.SaveAs("occupancy_" + os.path.basename(sys.argv[1]).replace(".root", ".png"))

tree.Draw("@HFDigiIPhi.size()>>size_hist")
size_hist.Draw();
canv.SaveAs("size_" + os.path.basename(sys.argv[1]).replace(".root", ".png"))
