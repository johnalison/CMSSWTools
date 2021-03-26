#!/bin/bash

#
#  2018
#
echo "!!!! WARNING: Submitting for Data 2018!!!!"
echo python submit_all.py \
  triggerStudy.py \
  -f dataSets/data2018.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_Data.root isMC=False globalTag=102X_upgrade2018_realistic_v21 \
  -o /store/user/johnda/hh4b/TriggerStudy \
  -l Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt \
  -v crab_Data2018

echo "!!!! WARNING: Submitting for MC 2018!!!!"
echo python submit_all.py \
  triggerStudy.py \
  -f dataSets/MC2018.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_MC_2018.root isMC=True globalTag=102X_upgrade2018_realistic_v20 \
  -o /store/user/johnda/hh4b/TriggerStudy \
  -v crab_MC2018


#
#  2017 
#
echo "!!!! WARNING: Submitting for Data 2017!!!!"
echo python submit_all.py \
  triggerStudy2017.py \
  -f dataSets/data2017.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_Data_2017.root isMC=False globalTag=94X_dataRun2_ReReco_EOY17_v2 \
  -o /store/user/johnda/hh4b/TriggerStudy \
  -l Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt  \
  -v crab_Data2017


echo "!!!! WARNING: Submitting for MC 2017!!!!"
echo python submit_all.py \
  triggerStudy2017.py \
  -f dataSets/MC2017.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_MC_2017.root isMC=True globalTag=94X_mc2017_realistic_v14 \
  -o /store/user/johnda/hh4b/TriggerStudy \
  -v crab_MC2017


#
#  2016
#
echo "!!!! WARNING: Submitting for Data 2016!!!!"
echo python submit_all.py \
  triggerStudy2016.py \
  -f dataSets/data2016.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_Data_2016.root isMC=False globalTag=80X_dataRun2_2016LegacyRepro_v4 \
  -o /store/user/johnda/hh4b/TriggerStudy \
  -l Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt \
  -v crab_Data2016


echo "!!!! WARNING: Submitting for MC 2016!!!!"
echo python submit_all.py \
  triggerStudy2016.py \
  -f dataSets/MC2016.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_MC_2016.root isMC=True globalTag=94X_mcRun2_asymptotic_v3 \
  -o /store/user/johnda/hh4b/TriggerStudy \
  -v crab_MC2016_v2
