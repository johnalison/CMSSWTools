#!/bin/bash


echo "!!!! WARNING: Submitting for Data 2018!!!!"
python submit_all.py \
  triggerStudy.py \
  -f dataSets/data2018.txt \
  -s T3_US_FNALLPC \
  -p outputFile=hist_Test.root isMC=False \
  -o /store/user/johnda/hh4b/TriggerStudy \
  -l Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt \
  -v crab_Data_v1
