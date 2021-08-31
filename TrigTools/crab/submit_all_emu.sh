#!/bin/bash

#
#  2018
#
echo "!!!! WARNING: Submitting for Data 2018!!!!"
echo python submit_all.py \
  triggerStudyEmu.py \
  -f dataSets/data2018MuonEG.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_Data.root isMC=False \
  -o /store/user/johnda/hh4b/TriggerStudyEMu \
  -l Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt \
  -v crab_Data2018MuonEg_inMJ

echo "!!!! WARNING: Submitting for MC 2018!!!!"
echo python submit_all.py \
  triggerStudyEmu.py \
  -f dataSets/MC2018TT2L2Nu.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_MC_2018.root isMC=True  \
  -o /store/user/johnda/hh4b/TriggerStudyEMu \
  -v crab_MC2018TT2L2Nu_inMJ


#
#  2017
#
echo "!!!! WARNING: Submitting for Data 2017!!!!"
echo python submit_all.py \
  triggerStudyEmu_2017.py \
  -f dataSets/data2017MuonEG.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_Data.root isMC=False \
  -o /store/user/johnda/hh4b/TriggerStudyEMu \
  -l Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt \
  -v crab_Data2017MuonEg_inMJ

echo "!!!! WARNING: Submitting for MC 2017!!!!"
echo python submit_all.py \
  triggerStudyEmu_2017.py \
  -f dataSets/MC2017TT2L2Nu.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_MC_2017.root isMC=True  \
  -o /store/user/johnda/hh4b/TriggerStudyEMu \
  -v crab_MC2017TT2L2Nu_inMJ



#
#  2016
#
echo "!!!! WARNING: Submitting for Data 2016!!!!"
echo python submit_all.py \
  triggerStudyEmu_2016.py \
  -f dataSets/data2016MuonEG.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_Data.root isMC=False \
  -o /store/user/johnda/hh4b/TriggerStudyEMu \
  -l Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt \
  -v crab_Data2016MuonEg_inMJ

echo "!!!! WARNING: Submitting for MC 2016!!!!"
echo python submit_all.py \
  triggerStudyEmu_2016.py \
  -f dataSets/MC2016TT2L2Nu.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_MC_2016.root isMC=True  \
  -o /store/user/johnda/hh4b/TriggerStudyEMu \
  -v crab_MC2016TT2L2Nu_inMJ

