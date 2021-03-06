#ifndef SimGeneral_MixingModule_DigiAccumulatorMixModFactory_h
#define SimGeneral_MixingModule_DigiAccumulatorMixModFactory_h

#include "FWCore/PluginManager/interface/PluginFactory.h"
#include "SimGeneral/MixingModule/interface/DigiAccumulatorMixMod.h"

namespace edm {
  class ConsumesCollector;
  class ParameterSet;
  namespace one {
    class EDProducerBase;
  }

  typedef DigiAccumulatorMixMod*(DAFunc)(ParameterSet const&, one::EDProducerBase&, ConsumesCollector&);
  typedef edmplugin::PluginFactory<DAFunc> DigiAccumulatorMixModPluginFactory;

  class DigiAccumulatorMixModFactory {
  public:
    ~DigiAccumulatorMixModFactory();

    static DigiAccumulatorMixModFactory const* get();

    std::auto_ptr<DigiAccumulatorMixMod>
      makeDigiAccumulator(ParameterSet const&, one::EDProducerBase&, ConsumesCollector&) const;

  private:
    DigiAccumulatorMixModFactory();
    static DigiAccumulatorMixModFactory const singleInstance_;
  };
}

#define DEFINE_DIGI_ACCUMULATOR(type) \
  DEFINE_EDM_PLUGIN (edm::DigiAccumulatorMixModPluginFactory,type,#type)
  //DEFINE_EDM_PLUGIN (edm::DigiAccumulatorMixModPluginFactory,type,#type); DEFINE_FWK_PSET_DESC_FILLER(type)

#endif

