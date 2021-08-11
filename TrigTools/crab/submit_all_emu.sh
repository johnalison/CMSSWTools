#!/bin/bash

#
#  2018
#
echo "!!!! WARNING: Submitting for Data 2018!!!!"
echo python submit_all.py \
  triggerStudyEmu.py \
  -f dataSets/data2018MuonEG.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_Data.root isMC=False globalTag=106X_dataRun2_v33 \
  -o /store/user/johnda/hh4b/TriggerStudyEMu \
  -l Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt \
  -v crab_Data2018MuonEg

echo "!!!! WARNING: Submitting for MC 2018!!!!"
echo python submit_all.py \
  triggerStudyEmu.py \
  -f dataSets/MC2018TT2L2Nu.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_MC_2018.root isMC=True globalTag=106X_upgrade2018_realistic_v15_L1v1 \
  -o /store/user/johnda/hh4b/TriggerStudyEMu \
  -v crab_MC2018TT2L2Nu

