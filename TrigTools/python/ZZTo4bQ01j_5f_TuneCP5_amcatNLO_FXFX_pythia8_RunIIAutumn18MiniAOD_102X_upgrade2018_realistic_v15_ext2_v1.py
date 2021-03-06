import FWCore.ParameterSet.Config as cms

ZZTo4b_source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/06A1A120-BC82-724B-8853-C5E30342C5F4.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/C4521F03-2B6F-7045-8EB7-9E24C08548E8.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/3FD95EDD-83AB-574C-8209-E6BBD122F13E.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/21217DA7-B0D2-0242-82F4-4427D78A4D70.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/97FCE896-E950-A44F-800A-C1CF158F5ACD.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/2657F543-591E-4E46-A968-33033C8210A5.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/A345E048-E2CF-D241-966F-49EDDC83D203.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/7624D94C-043A-2341-9D12-411C4E3A3B88.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/2EB51845-3C00-1346-9A1D-3354C71DD317.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/1C32E910-7AAC-6748-9B5D-7F0FFD62F40E.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/D5769BAE-D30B-694F-AD26-CC870EC14631.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/8857283B-D066-8F4A-BEF6-492FE67E8F0E.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/0C80A665-BCC4-934B-8BDD-65EDA958E0BB.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/4C0641B1-82C9-DE4A-A379-3E0D0DD1BB81.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/2F38FF74-F9D7-A948-B089-C9F8CB6A7B6A.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/121B6584-8BA2-5648-AB66-95D107A061EC.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/7D47A1A7-BB07-3849-B96E-9A3C298C253A.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/390785AF-ECD5-3B49-972B-71FAFD4097D8.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/9B84F5AE-95E4-E04F-9619-405C5778AAC9.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/D5A9A855-E074-0144-BA10-F379D038F00E.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/1CF4DC7A-E0A3-9445-9FB1-5546B6CC1EDA.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/F25C4FFE-7CA0-B84C-8D4D-BC1CB0E591A9.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/8D06D954-B138-E342-96DB-6216C0A55135.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/EB502526-C63C-4D44-B16A-B7D85A10172B.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/CEE0CDAE-B7F8-2F42-A3FD-689EB980B1E4.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/09B54250-390D-E347-A782-979A8DBA3F84.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/15D67D29-95BC-6B45-A890-E1DF4CFB3FE2.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/0DC71B83-5ABF-894A-A1F0-759D06A4F69E.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/C21E2DE1-2193-3243-89B4-261800AD708B.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/2C9F1014-87B6-F44A-8FB9-2E5040731604.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/52215391-562F-9B43-9E3C-0E0A4709244C.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/38C922CF-C1F6-C644-9F17-08BE8027A01A.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/EC8B023F-ADB7-A043-9945-0976272940FB.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/8B71F2F7-A3FB-5046-97C1-43C105F1249B.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/9AA5DAA9-61F3-D040-8F19-4184CEA00262.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/312502FB-E4FC-8F45-9C4A-DAF44F72A8FB.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/45948246-EB9F-5A47-930C-7FF9B03D876E.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/0D80D341-7082-E048-A1EB-8EF586802F8B.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/64B6FA71-B22C-1C4F-8135-14715EF6A709.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/8F722026-6C9A-5147-B868-47E1C80174B9.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/6F46B6AB-9774-7442-AC64-9E0E4898873C.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/5E0DCF0D-A6ED-6E4E-AE08-BFF72E9FAB72.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/B941C258-9501-864A-B71B-770706621F35.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/01E9EBB4-AF3E-AE44-90A2-7B13FC715911.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/B2E056F0-2D43-664F-8997-0349BFC60799.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/0B209604-E587-164F-8D73-0B0102830EE0.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/41404DD0-6D5F-CD41-9DAD-A62F998308C0.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/2B06C6A2-5170-F14C-A315-180D353EBC61.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/37B3152D-3601-9D4C-B79D-B905CB13996D.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/BBFAFEC8-D3D6-DD41-B86B-9793E0080833.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/CC6AF8E8-953C-784C-8892-618E7F4889B8.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/52E22E87-634B-914F-914C-5522E36ED45F.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/AA0F849D-1B65-B447-8A51-53A7222770CC.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/7F3D04FD-1A59-4045-B179-68B7E73EC01E.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/CC627D88-A8EB-0146-9B50-1417A1E98444.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/C33CEB0E-63F6-3D4F-8610-916364754D86.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/AE53B9D1-7ED5-5744-8D0C-2BC5A29AC7C7.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/D703BEB5-C829-3043-B02E-DA020192C0FD.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/28E63C58-07AE-E14A-919B-11B3ED698B63.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/CB54DB76-1C92-2F46-9AAE-A87EA525CB16.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/5747D3F6-14BA-6E49-936C-2B7A8CFF45EC.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/6CA42ACD-EA45-5241-B766-766D2BAC628D.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/CD6E1C5A-02FD-144B-965B-83D9921E969E.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/941D65C4-0011-1B45-A893-817B26B3BFB3.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/277FDB25-B9C9-C346-8300-51EBBA1BF740.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/9F8DE64E-BD3B-A846-845F-43319798E314.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/E50113CB-2C31-854B-AEAF-5865F9D52F4C.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/240350B0-5D13-3E40-B5F5-4B3AD52E688B.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/20BDD421-AE1F-E140-AC62-730CF12A9306.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/4D070A90-1117-7747-9AD9-FAE989BAE472.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/AB607880-E207-8446-B241-AA516F7638BB.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/96B613F2-C23E-7641-B00F-9C09CE221190.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/1601C728-CDFB-9A45-A92B-6AAAAA0C7BAB.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/DED84080-2F8A-554A-88D3-70DC6D7966AE.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/001D7B4F-4239-FC4E-8D4A-6BD365015939.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/F954D889-DCF7-4541-9D6D-9F4690EB7E98.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/1A16F9DB-3470-8E44-BC3A-CA0E4766F4BC.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/5ABC97F6-B766-F543-BF66-301AB251D154.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/96B9581B-683E-8343-9863-075555ADF074.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/69ED7820-074D-9840-A5CB-524F04AE814D.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/0CBC3BDC-CB0C-B242-832C-A3787C785DD6.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/AA29E133-BF2F-1647-8DE4-CE57DEE30FFD.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/0344708D-0AC7-FE46-953B-2A41F2B9AA52.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/21D8114B-F527-E54B-B1C4-C606B64950B8.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/AF5A0C78-8EE6-6245-AB28-E13A47253AAF.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/DA4DC5F2-41CA-4D4D-A2C8-5F890CE0AE8B.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/8E4DFA86-CB93-144F-B1F1-9EE67119A560.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/C87526C8-7089-1843-B1AA-DFB48905C703.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/251A373F-1840-1447-9D0D-F2E04E4AFF9B.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/956584E6-BE74-8240-A9C1-517C15BDBE3A.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/2B4278A3-70BF-AB45-A4D4-1F98F9877C00.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/9940564D-2018-C940-90B6-459EB2931926.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/48FDABB8-D283-FF49-9574-8D80E03696E1.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/D95A66EF-BB3C-BF4F-A831-3F363089C7DC.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/C3083497-2243-674B-B0E3-C648CE409B3F.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/D5F3E863-D319-514F-AB75-68DC6E13125D.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/BAB84D2C-2B14-9B44-96DA-20F694EACE5D.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/5AC7B66C-BFE8-B04F-AA6E-A1FB92403337.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/7815C64F-C788-2D42-BD56-0CB2F418DD26.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/FA3D3F1F-F859-9A4C-9193-97B1818368F9.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/348AB750-2FB8-5043-800D-841A09BF924B.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/47E90B0E-3B9C-5643-B404-3A87119BE4CC.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/61627CB7-9C7C-B847-B8EB-939E61855C0F.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/7CAD3FAF-D91A-2C4C-8C68-7ACABDF97366.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/40084BC1-2231-004C-A005-7523E3C0FDAA.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/83190119-722A-C44C-9E76-B27311B610FD.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/AC3784FE-6750-974F-B425-B7D4934125C1.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/25FBC738-FE20-2648-8626-9670C8E6F45A.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/28E6790C-5ED2-A447-92BB-F274F7FF096D.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/DFF9B9D5-51A4-DA4C-A1DC-46C5E1AB90A5.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/3B22B7C8-18D2-D648-B3F4-C26793DB1B33.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/53B23577-97B4-FE4B-9CE0-2872DD235135.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/17BF537D-EB1D-2D4A-8A7B-15C625565415.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/7D8FC171-C5B5-7145-932D-0ADB5C67A39E.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/FE664D2A-0674-AC4B-AFE9-0BDB4FF81B6F.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/7D8F3602-891B-9F4A-98BA-D20FB7CC990D.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/E01AE60C-FE9D-9F4C-8B80-617AB6BE0171.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/9B387D38-FBFE-7644-87F5-235F3227A0B2.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/F29E1007-CA21-C143-8052-297416C254D3.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/EB4A67C0-FB15-D04B-A909-369DD2AF2101.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/4C10888C-736A-9F41-92C0-DE2AAE72EA56.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/E119C4D2-29E1-884C-9CB6-B2447666E1B4.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/29456CA8-AEF3-8149-BBA6-2A22921B9F14.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/C6627DF7-5CC4-2B4C-A1F3-6506B018C420.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/304E266D-B834-FC4D-B970-8CC2C4688A3D.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/F2F66410-E006-7843-9AB5-08D3EEFBA8E9.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/36FF0D83-174B-924D-A825-DC97A6A17947.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/B4A07FA5-BBFB-1B41-8DEC-B3B9201766D4.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/0354256F-1B90-2840-9761-9A23F1D666A9.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/48F2B751-7321-6C42-B8A6-3ACA68FF9405.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/429225C8-74FE-2741-B174-80B2AF1C2B00.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/0193BC3B-E42A-8942-AD63-9CEE6FAD9A8E.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/1A3F1B28-FA28-C14B-829E-EE348525781A.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/DF2879E7-5FC1-9F42-9B66-5E4F45B9F08D.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/DB55CE92-9793-204C-A8BC-39A605CAA378.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/88711DD8-0C7A-DE46-9BCA-ACC51DEC9743.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/A63DAEF5-830A-EB40-9FB2-0DBEEB93BE25.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/9CB39A51-24BC-CC4E-9283-7AF83AE8F2EE.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/140FB80E-940D-4F4F-85C5-C1E13CEDDEC7.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/130000/85444FCC-E215-A84A-9A9F-E9F7338549B1.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/CDFF66B7-72D5-A14B-BB97-FC87B760161F.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/43A6DBD6-DAC0-8343-B889-B8A45F59406B.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/D5972393-97AA-9646-AF6E-034A0AB2F315.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/1FD44258-2611-D143-8E1E-72C21DCAEC7A.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/4FD9576A-2AB3-AA46-94BC-3C313084A69D.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/E1143AE8-42A8-914C-B6E6-CF5A1FEE0F93.root",
        "/store/mc/RunIIAutumn18MiniAOD/ZZTo4bQ01j_5f_TuneCP5_amcatNLO_FXFX_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/260000/95A2D3EA-5BCD-B940-9CBB-CEAA6C20A674.root",
    )
)
