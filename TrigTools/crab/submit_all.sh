#!/bin/bash


#echo "!!!! WARNING: Submitting for Data 2018!!!!"
python submit_all.py \
  triggerStudy.py \
  -f dataSets/data2018.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_Data.root isMC=False globalTag=102X_upgrade2018_realistic_v21 \
  -o /store/user/johnda/hh4b/TriggerStudy \
  -l Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt \
  -v crab_Data_wL1_v2
