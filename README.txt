check the following situations, using this "full" FED list:
 
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

Test b:
=======

xrdcp root://xrootd.unl.edu//store/data/Run2012A/Jet/RAW/v1/000/190/646/12E499AE-E480-E111-9BAF-003048D3733E.root /tmp/${USER}/file.root

cmsRun analysis_utca_compare_test_cfg.py \
inputFiles="file:///tmp/${USER}/file.root" \
outputFile="outputFile_190646_vmeutcaEmap.root" \
emap="vme+utca" \
processEvents=1

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
