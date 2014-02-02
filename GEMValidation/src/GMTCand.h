#ifndef GEMValidation_GMTCand_h
#define GEMValidation_GMTCand_h

#include "GEMCode/GEMValidation/src/GMTRegCand.h"

class GMTCand //: public GMTRegCand
{
 public:
  /// constructor
  GMTCand();
  /// copy constructor
  GMTCand(const GMTCand&);
  /// destructor
  ~GMTCand();

  /*  
  init(const L1MuRegionalCand *t, CSCTFPtLUT* ptLUT, 
       edm::ESHandle< L1MuTriggerScales > &muScales, 
       edm::ESHandle< L1MuTriggerPtScale > &muPtScale);
  */
  //  const L1MuRegionalCand * l1cand;
  GMTRegCand* gmtRegCand();
  
 private:
  double pt_;
  double eta_;
  double phi_;
  double dr_;
};

#endif
