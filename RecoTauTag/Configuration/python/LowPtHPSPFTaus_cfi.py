import FWCore.ParameterSet.Config as cms
import PhysicsTools.PatAlgos.tools.helpers as configtools

def addLowPtTaus(process):
    from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet
    from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag

    process.load("RecoTauTag.Configuration.LowPtHPSPFTaus_cff")
    patAlgosToolsTask = configtools.getPatAlgosToolsTask(process)
    patAlgosToolsTask.add(process.LowPtHPSPFTausTask)

    process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")
    process.ptau = cms.Path( process.PFTau )
    process.PATTauSequence = cms.Sequence(process.PFTau+process.makePatTaus+process.selectedPatTaus)
    process.PATTauSequenceLowPt = cloneProcessingSnippet(process,process.PATTauSequence, "LowPt", addToTask = True)
    process.recoTauAK4PFJets08RegionLowPt.src = cms.InputTag('ak8PFJetsLowPt')
    process.recoTauAK4PFJets08RegionLowPt.pfCandSrc = cms.InputTag('particleFlow')
    process.recoTauAK4PFJets08RegionLowPt.pfCandAssocMapSrc = cms.InputTag('ak8PFJetsLowPt', 'pfCandAssocMapForIsolation')
    process.recoTauAK4PFJets08RegionLowPt.minJetPt = cms.double(1.0)  
    process.selectedPatTausLowPt.cut = cms.string("pt > 1. && tauID(\'decayModeFindingNewDMs\')> 0.5")#tau pt> 1 GeV of threshold output

    process.ak4PFJetsLegacyHPSPiZerosLowPt.jetSrc = cms.InputTag('ak8PFJetsLowPt')
    process.ak4PFJetsLegacyHPSPiZerosLowPt.minJetPt = cms.double(1) #jet pt> 1 GeV of threshold in input
    process.ak4PFJetsRecoTauChargedHadronsLowPt.jetSrc = cms.InputTag('ak8PFJetsLowPt')
    #process.ak4PFJetsRecoTauChargedHadronsLowPt.builders[1].dRcone = cms.double(0.3) # to be checked
    #process.ak4PFJetsRecoTauChargedHadronsLowPt.builders[1].dRconeLimitedToJetArea = cms.bool(True)

    process.combinatoricRecoTausLowPt.jetSrc = cms.InputTag('ak8PFJetsLowPt')

# CG Added on 19.02.2019
    process.ak4PFJetsRecoTauChargedHadronsLowPt.minJetPt = cms.double(1.0)
#CG possible modification wanted:
    process.hpsPFTauPrimaryVertexProducerLowPt.cut = cms.string('pt > 18.0 & abs(eta) < 2.4')




    _allModifiers = cms.VPSet()
    for modifier in process.combinatoricRecoTausLowPt.modifiers:
        _allModifiers.append(modifier)
    process.combinatoricRecoTausLowPt.modifiers.remove(process.combinatoricRecoTausLowPt.modifiers[3])
    from Configuration.Eras.Modifier_run2_miniAOD_80XLegacy_cff import run2_miniAOD_80XLegacy
    from Configuration.Eras.Modifier_run2_miniAOD_94XFall17_cff import run2_miniAOD_94XFall17
    for era in [ run2_miniAOD_80XLegacy, run2_miniAOD_94XFall17]:
        era.toModify(process.combinatoricRecoTausLowPt, modifiers = _allModifiers)
    process.combinatoricRecoTausLowPt.builders[0].pfCandSrc = cms.InputTag('particleFlow')
    ## Note JetArea is not defined for subjets (-> do not switch to True in hpsPFTauDiscriminationByLooseMuonRejection3LowPt, False is default)
    ## The restiction to jetArea is turned to dRMatch=0.1 (-> use explicitly this modified value)
    #process.hpsPFTauDiscriminationByLooseMuonRejection3LowPt.dRmuonMatch = 0.1
    #process.hpsPFTauDiscriminationByTightMuonRejection3LowPt.dRmuonMatch = 0.1  
    massSearchReplaceAnyInputTag(process.PATTauSequenceLowPt,cms.InputTag("ak4PFJets"),cms.InputTag("ak8PFJetsLowPt"))  
    process.slimmedTausLowPt = process.slimmedTaus.clone(src = cms.InputTag("selectedPatTausLowPt"))
    patAlgosToolsTask.add(process.slimmedTausLowPt)

    return process
