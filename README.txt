Here is the sequence of steps:
1) [ongoing Mar. 9] merge these PRs:
https://github.com/cms-sw/cmssw/pull/7950
https://github.com/cms-sw/cmssw/pull/8103

2) [finished Mar. 4] validate series G emap (Dick, Hua, et al.)

3) [ongoing Mar. 9] upload and use series G emap.
The inclusion of uTCA channels will not do harm, 
when the unpacker's list of FEDs contains only VME FEDs.
See notes below.

4) [ongoing Mar. 9] stabilize CDAQ readout of uTCA FEDs

5) update the unpacker's list of FEDs from (700-731), to (700-731, 1118, 1120, 1122)

6) check the following situations, using this "full" FED list:
 
test | data  |   e-map    |  CDAQ includes  |   desired digis	|  run number  | status 
     |       |            |   HBHE   HF     |    HBHE    HF	|      	       |        
-----+-------+------------+-----------------+-------------------+--------------+--------
a      Run 1      VME         VME    VME         VME    VME	   190646	  DONE
b      Run 1    VME+uTCA      VME    VME         VME    VME	   190646	  DONE
c       LS 1      VME         VME    VME         VME    VME	   234628	  DONE
d       LS 1    VME+uTCA      VME    VME         VME    VME	   234628	  DONE
e       LS 1      VME         VME  VME+uTCA      VME    VME	   235316	  DONE
f       LS 1    VME+uTCA      VME  VME+uTCA      VME    uTCA	   235316	  DONE
g       LS 1      VME         VME   uTCA         VME    empty	   237318	  DONE
h       LS 1    VME+uTCA      VME   uTCA         VME    uTCA	   237318	  DONE

Test a:
=======

xrdcp root://xrootd.unl.edu//store/data/Run2012A/Jet/RAW/v1/000/190/646/12E499AE-E480-E111-9BAF-003048D3733E.root /tmp/${USER}/file.root

cmsRun analysis_utca_compare_test_cfg.py \
inputFiles="file:///tmp/${USER}/file.root" \
outputFile="outputFile_190646_vmeOnlyEmap.root" \
emap="vme" \
processEvents=1

* seg fault *

Test b:
=======

xrdcp root://xrootd.unl.edu//store/data/Run2012A/Jet/RAW/v1/000/190/646/12E499AE-E480-E111-9BAF-003048D3733E.root /tmp/${USER}/file.root

cmsRun analysis_utca_compare_test_cfg.py \
inputFiles="file:///tmp/${USER}/file.root" \
outputFile="outputFile_190646_vmeutcaEmap.root" \
emap="vme+utca" \
processEvents=1

* seg fault *

Test c:
=======

cmsRun analysis_utca_compare_test_cfg.py \
inputFiles="root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/234/628/00000/18271693-CAB6-E411-AF94-02163E01274B.root" \
outputFile="outputFile_234628_vmeOnlyEmap.root" \
emap="vme" \
processEvents=1

Test d:
=======

cmsRun analysis_utca_compare_test_cfg.py \
inputFiles="root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/234/628/00000/18271693-CAB6-E411-AF94-02163E01274B.root" \
outputFile="outputFile_234628_vmeutcaEmap.root" \
emap="vme+utca" \
processEvents=1

Test e:
=======

cmsRun analysis_utca_compare_test_cfg.py \
inputFiles="root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/236/445/00000/522FB2AC-F5C0-E411-8841-02163E01221B.root" \
outputFile="outputFile_236445_vmeOnlyEmap.root" \
emap="vme" \
processEvents=1

Test f:
=======

cmsRun analysis_utca_compare_test_cfg.py \
inputFiles="root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/236/445/00000/522FB2AC-F5C0-E411-8841-02163E01221B.root" \
outputFile="outputFile_236445_vmeutcaEmap.root" \
emap="vme+utca" \
processEvents=1

Test g:
=======

cmsRun analysis_utca_compare_test_cfg.py \
inputFiles="root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/237/318/00000/24F11386-94C6-E411-96AC-02163E012078.root" \
outputFile="outputFile_237318_vmeonlyEmap.root" \
emap="vme" \
processEvents=1

Test h:
=======

cmsRun analysis_utca_compare_test_cfg.py \
inputFiles="root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/237/318/00000/24F11386-94C6-E411-96AC-02163E012078.root" \
outputFile="outputFile_237318_vmeutcaEmap.root" \
emap="vme+utca" \
processEvents=1



7) make a pull request with the updated FED list, e.g.
https://github.com/cms-sw/cmssw/compare/CMSSW_7_5_X...elaird:hf-utca

8) add a second unpacker instance to the DQM, to facilitate VME-uTCA comparison:
https://github.com/cms-sw/cmssw/blob/CMSSW_7_5_X/DQM/Integration/python/test/hcal_dqm_sourceclient-live_cfg.py

9) make a pull request for 8

10a) Move the HF FE data ribbons from VME crates 9 and 12 to uTCA crates 29 and 32.
10b) Leave split the 1/3 of HF FE fibers that are currently split to VME crate 2 and uTCA crate 22.
10c) Remove FEDs 720,721,722,723 from the CDAQ configuration.



OLD, DISFAVORED PROPOSAL
------------------------
5a) move the HF FE data ribbons from VME crates 9 and 12 to uTCA crates 29 and 32.
Leave split the 1/3 of HF FE fibers that are currently split to VME crate 2 and uTCA crate 22.

5b) at the same time as 5a, update the unpacker's list of FEDs from
700-731, to 700-717, 724-731, 1118, 1120, 1122

6) [optional, but useful] instantiate another unpacker, to unpack FEDs 718-719,
into a "reference/legacy" collection of digis.  This would perhaps make it more convenient for HCAL and trigger emulator experts to debug the behavior of uTCA crate 22, using VME crate 2 as a reference.



NOTES
-----
Edmund ran CMSSW with a few configurations on Feb. 24-5.  All of the configurations used an emap with both VME and uTCA channels included.

1) FED list has only HF VME FEDs (700 series): no problem
2) FED list has only HF uTCA FEDs (1100 series): no problem
3) FED list has HF VME + HF uTCA: uTCA digis seemed to "clobber" VME
digis; we did not fully investigate the behavior
4) one unpacker instance with only HF VME FEDs; simultaneously,
another unpacker instance with only HF uTCA FEDs: one collection of
VME digis; one collection of uTCA digis: no problem
5) FED list contains 700-717 (VME HBHE) + 1118,1120,1122 (HF
uTCA) + 724-731 (VME HO): no problem
