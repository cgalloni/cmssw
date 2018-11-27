#Low pt tau v2

```
cmsrel  CMSSW_9_4_7
cd CMSSW_9_4_7/src
cmsenv
git cms-init
git cms-addpkg PhysicsTools/PatAlgos
git cms-addpkg RecoTauTag/Configuration
scram b -j 8
git remote add cgalloni https://github.com/cgalloni/cmssw
git fetch cgalloni
git checkout -b new_branch  cgalloni/LowPtTaus

```

change jet seeding for taus: 

RecoTauTag/Configuration/python/LowPtHPSPFTaus_cff.py



list of changed files wrt CMSSW_9_7_4:

RecoTauTag/Configuration/python/LowPtHPSPFTaus_cff.py
RecoTauTag/Configuration/python/LowPtHPSPFTaus_cfi.py

PhysicsTools/PatAlgos/python/slimming/miniAOD_tools.py
PhysicsTools/PatAlgos/python/slimming/MicroEventContent_cff.py

