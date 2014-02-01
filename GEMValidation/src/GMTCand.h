#ifndef GEMValidation_GMTCand_h
#define GEMValidation_GMTCand_h

class GMTCand : GMTRegCand
{
 public:
  GMTCand();
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
