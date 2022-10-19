# RecoBTag-PerformanceMeasurements


## Basics & software setup

```bash
# setting up the latest release

#!/bin/bash
cmsrel CMSSW_12_4_10

cd CMSSW_12_4_10/src

cmsenv
git-cms-init

git clone git@github.com:johnalison/CMSSWTools.git
git clone git@github.com:johnalison/TriggerEmulator.git

scram b -j12

```

## Command to run loccal

```bash
> cmsRun CMSSWTools/TrigTools/test/triggerStudyEmu.py isMC=True outputFile=histTestMCEmu.root maxEvents=10000

```