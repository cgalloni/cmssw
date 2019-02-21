import FWCore.ParameterSet.Config as cms
import copy


'''
Sequences for reconstructing LowPt taus using the HPS algorithm

'''

import CommonTools.ParticleFlow.pfNoPileUp_cff as LowPtTaus
pfPileUpForLowPtTaus = LowPtTaus.pfPileUp.clone(
    PFCandidates = cms.InputTag('particleFlow'),
    checkClosestZVertex = cms.bool(False)
)
pfNoPileUpForLowPtTaus = LowPtTaus.pfNoPileUp.clone(
    topCollection = cms.InputTag('pfPileUpForLowPtTaus'),
    bottomCollection = cms.InputTag('particleFlow')
)


import RecoJets.JetProducers.ak4PFJets_cfi as LowPtTaus2

# reclustering ak8 
betapar = cms.double(0.0)
fatjet_ptmin = 1.0


LowPtTauSeeds = LowPtTaus2.ak4PFJets.clone(     
    doAreaFastjet = cms.bool(True),
    rParam = cms.double(0.8),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin =  cms.double(fatjet_ptmin),   
)


from Configuration.Eras.Modifier_pp_on_XeXe_2017_cff import pp_on_XeXe_2017
pp_on_XeXe_2017.toModify(LowPtTauSeeds, inputEtMin = 999999.0)

LowPtHPSPFTausTask = cms.Task(
    pfPileUpForLowPtTaus,
    pfNoPileUpForLowPtTaus,
    LowPtTauSeeds
)

'''
import CommonTools.ParticleFlow.pfNoPileUp_cff as lowptTaus
pfPileUpForLowptTaus = lowptTaus.pfPileUp.clone(
    PFCandidates = cms.InputTag('particleFlow'),
    checkClosestZVertex = cms.bool(False)
)
pfNoPileUpForLowptTaus = lowptTaus.pfNoPileUp.clone(
    topCollection = cms.InputTag('pfPileUpForLowptTaus'),
    bottomCollection = cms.InputTag('particleFlow')
)


import RecoJets.JetProducers.ak4PFJets_cfi as lowptTaus2
import RecoJets.JetProducers.CMSBoostedTauSeedingParameters_cfi as lowptTaus3
ca8PFJetsCHSprunedForLowptTaus = lowptTaus2.ak4PFJets.clone(
    lowptTaus3.CMSBoostedTauSeedingParameters,
    #src = cms.InputTag('pfNoPileUpForBoostedTaus'),
    jetPtMin = cms.double(100.0),
    doAreaFastjet = cms.bool(True),
    nFilt = cms.int32(100),
    rParam = cms.double(0.8),
    jetAlgorithm = cms.string("CambridgeAachen"),
    writeCompound = cms.bool(True),
    jetCollInstanceName = cms.string('subJetsForSeedingLowptTaus')
)

from Configuration.Eras.Modifier_pp_on_XeXe_2017_cff import pp_on_XeXe_2017
pp_on_XeXe_2017.toModify(ca8PFJetsCHSprunedForLowptTaus, inputEtMin = 999999.0)

LowPtTauSeeds = cms.EDProducer("BoostedTauSeedsProducer",
    subjetSrc = cms.InputTag('ca8PFJetsCHSprunedForLowptTaus', 'subJetsForSeedingLowptTaus'),
    pfCandidateSrc = cms.InputTag('particleFlow'),
    verbosity = cms.int32(0)
)

LowPtHPSPFTausTask = cms.Task(
    pfPileUpForLowptTaus,
    pfNoPileUpForLowptTaus,
    ca8PFJetsCHSprunedForLowptTaus,
    LowPtTauSeeds
)
'''
