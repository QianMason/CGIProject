/*
# This file is part of Primer Pooler v1.41 (c) 2016-18 Silas S. Brown.  For Wen.
# 
# This program is free software; you can redistribute and
# modify it under the terms of the General Public License
# as published by the Free Software Foundation; either
# version 3 of the License, or any later version.
#
# This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY.  See the GNU General
# Public License for more details.
*/
/* thirty-two to sixty-four dot h is automatically generated
   from sixty-four to one-hundred-and-twenty-eight dot h,
   with these two numbers halved throughout.

   These files should be included ONLY by bit-common.h.
   The general interface is in all-primers.h.
*/

enum { PrimerLimit = 64 }; /* max length of a primer */
typedef struct {
  union { /* array of primers read "forward" (5'-3') */
    MaybeDegeneratePrimer32* p32;
    MaybeDegeneratePrimer64* p64;
  } forward;
  union { /* same primers read "backward" (3'-5')
             (not to be confused with "reverse primer") */
    MaybeDegeneratePrimer32* p32;
    MaybeDegeneratePrimer64* p64;
  } backward;
  union { /* array of tags (read 5'-3') */
    MaybeDegeneratePrimer32* p32;
    MaybeDegeneratePrimer64* p64;
  } tags;
  int *whichTag; /* which tag no. applies to primer N (-1 for none) */
  char* *names; /* pointers to primer names */
  void *rawData; /* for above pointers to point into */
  int np;     /* total number of primers */
  int maxLen; /* length of longest primer */
} AllPrimers;
void freeAllPrimers(AllPrimers ap) {
  if(ap.np >= 0) {
    free(ap.names); free(ap.forward.p32);
    free(ap.backward.p32); free(ap.tags.p32);
    free(ap.whichTag); free(ap.rawData);
  }
}
static inline int sizeofMDPrimer(int maxLen) {
  return (maxLen <= 32) ? sizeof(MaybeDegeneratePrimer32):sizeof(MaybeDegeneratePrimer64);
}
AllPrimers loadFASTA(FILE *f) {
  AllPrimers r; /* sets r.np=-1 on failure */
  char *loadAndClose(FILE *f);
  int numPrimers(const char*,int*,int*); /*load-common.c*/
  r.rawData = loadAndClose(f);
  if(!r.rawData) {
    fputs("Could not load file\n",stderr); r.np = -1;
    return r;
  }
  int numTags=0;
  r.np = numPrimers(r.rawData, &r.maxLen, &numTags);
  if(r.np<0) return r; /* err already printed */
  r.forward.p32 = malloc(r.np * sizeofMDPrimer(r.maxLen));
  r.backward.p32 = malloc(r.np*sizeofMDPrimer(r.maxLen));
  r.whichTag = malloc(r.np*sizeof(int));
  r.tags.p32 = calloc(numTags,sizeofMDPrimer(r.maxLen));
  r.names = malloc(r.np*sizeof(char*));
  if(memFail(r.forward.p32,r.backward.p32,r.tags.p32,r.names,r.rawData,_memFail)) { r.np=-1; return r; }
  if(r.maxLen <= 32) {
    parseFASTA32(r.rawData,r.forward.p32,r.tags.p32,r.whichTag,r.names);
    int i; for(i=0; i<r.np; i++) r.backward.p32[i] = MaybeDegeneratePrimerReverse32(r.forward.p32[i]);
  }
  else {
    parseFASTA64(r.rawData,r.forward.p64,r.tags.p64,r.whichTag,r.names);
    int i; for(i=0; i<r.np; i++) r.backward.p64[i] = MaybeDegeneratePrimerReverse64(r.forward.p64[i]);
  }
  return r;
}
void addTags(AllPrimers ap) {
  int i;
  if(ap.maxLen <= 32)
    for(i=0; i<ap.np; i++) if(ap.whichTag[i]>=0) {
      MaybeDegeneratePrimer32 tag=ap.tags.p32[ap.whichTag[i]];
      MaybeDegeneratePrimerTag32(ap.forward.p32+i,tag);
      MaybeDegeneratePrimerTag32B(ap.backward.p32+i,tag);
    }
  else
    for(i=0; i<ap.np; i++) if(ap.whichTag[i]>=0) {
      MaybeDegeneratePrimer64 tag=ap.tags.p64[ap.whichTag[i]];
      MaybeDegeneratePrimerTag64(ap.forward.p64+i,tag);
      MaybeDegeneratePrimerTag64B(ap.backward.p64+i,tag);
    }
}
void removeTags(AllPrimers ap) {
  int i;
  if(ap.maxLen <= 32)
    for(i=0; i<ap.np; i++) if(ap.whichTag[i]>=0) {
      MaybeDegeneratePrimer32 tag=ap.tags.p32[ap.whichTag[i]];
      MaybeDegeneratePrimerRmTag32(ap.forward.p32+i,tag);
      MaybeDegeneratePrimerRmTag32B(ap.backward.p32+i,tag);
    }
  else
    for(i=0; i<ap.np; i++) if(ap.whichTag[i]>=0) {
      MaybeDegeneratePrimer64 tag=ap.tags.p64[ap.whichTag[i]];
      MaybeDegeneratePrimerRmTag64(ap.forward.p64+i,tag);
      MaybeDegeneratePrimerRmTag64B(ap.backward.p64+i,tag);
    }
}
void printCounts(AllPrimers ap,FILE *f) {
  if(ap.maxLen <= 32)
    counts32(ap.forward.p32,ap.backward.p32,ap.np,f);
  else counts64(ap.forward.p64,ap.backward.p64,ap.np,f);
}
int printPooledCounts(AllPrimers ap,const int *pools,const int *precalcScores) { /* precalcScores==NULL ok */
  if(ap.maxLen <= 32)
    return pCounts32(ap.forward.p32,ap.backward.p32,ap.np,pools,precalcScores);
  else return pCounts64(ap.forward.p64,ap.backward.p64,ap.np,pools,precalcScores);
}
void printBonds(AllPrimers ap,FILE *f,int threshold,const int *pools) {
  if(ap.maxLen <= 32)
    printBonds32(ap.forward.p32,ap.backward.p32,ap.np,f,threshold,ap.names,pools);
  else printBonds64(ap.forward.p64,ap.backward.p64,ap.np,f,threshold,ap.names,pools);
  if (f!=stdout) fclose(f);
}
int* triangle(AllPrimers ap) {
  if(ap.maxLen <= 32)
    return triangle32(ap.forward.p32,ap.backward.p32,ap.np);
  else return triangle64(ap.forward.p64,ap.backward.p64,ap.np);
}

void printFASTA(AllPrimers ap,FILE *f,const int *pools,const int poolNo);
void printBasesMaybeD(AllPrimers ap,int n,FILE *f) {
  if(ap.maxLen <= 32)
    printBases32MaybeD(ap.forward.p32[n],f);
  else printBases64MaybeD(ap.forward.p64[n],f);
}

int NumPossibilities_32bases(AllPrimers ap,int n) {
  /* forward or backward should yield same result */
  if(ap.maxLen <= 32) return NumPossibilities32MaybeD_32bases(ap.forward.p32[n]);
  else return NumPossibilities64MaybeD_32bases(ap.forward.p64[n]);
}
int Make2bit(AllPrimers ap,int n,int useBackward,int doComplement,ULL *out,ULL *outValid,int possNo,int nPoss) {
  if(ap.maxLen <= 32) {
    MaybeDegeneratePrimer32 p = useBackward ? ap.backward.p32[n] : ap.forward.p32[n];
    if(doComplement) PrimerComplement32MaybeD(&p);
    return Make2bitFrom32D(upgradeToDegenerate32(p),out,outValid,possNo,nPoss);
  } else {
    MaybeDegeneratePrimer64 p = useBackward ? ap.backward.p64[n] : ap.forward.p64[n];
    if(doComplement) PrimerComplement64MaybeD(&p);
    return Make2bitFrom64D(upgradeToDegenerate64(p),out,outValid,possNo,nPoss);
  }
}

void dGprintBonds(AllPrimers ap,FILE *f,float threshold,const int *pools,const float *table) {
  if(ap.maxLen <= 32)
    dGprintBonds32(ap.forward.p32,ap.backward.p32,ap.np,f,threshold,ap.names,pools,table);
  else dGprintBonds64(ap.forward.p64,ap.backward.p64,ap.np,f,threshold,ap.names,pools,table);
  if (f!=stdout) fclose(f);
}
int* dGtriangle(AllPrimers ap,const float *table) {
  if(ap.maxLen <= 32)
    return dGtriangle32(ap.forward.p32,ap.backward.p32,ap.np,table);
  else return dGtriangle64(ap.forward.p64,ap.backward.p64,ap.np,table);
}
int dGprintPooledCounts(AllPrimers ap,const int *pools,const int *precalcScores,FILE *f) {
  if(ap.maxLen <= 32)
    return dGpCounts32(ap.np,pools,precalcScores,f);
  else return dGpCounts64(ap.np,pools,precalcScores,f);
}
void dGandScoreCounts(AllPrimers ap,const float *table,FILE *f) {
  if(ap.maxLen <= 32)
    return dGsCounts32(ap.forward.p32,ap.backward.p32,ap.np,table,f);
  else return dGsCounts64(ap.forward.p64,ap.backward.p64,ap.np,table,f);
}

void printStats(AllPrimers ap,const int *pools,const int *precalcScores,FILE *f) { /* precalcScores==NULL ok */
  if(ap.maxLen <= 32)
    pStats32(ap.forward.p32,ap.backward.p32,ap.np,pools,precalcScores,f);
  else pStats64(ap.forward.p64,ap.backward.p64,ap.np,pools,precalcScores,f);
}
void dGprintStats(AllPrimers ap,const int *pools,const int *precalcScores,FILE *f) { /* precalcScores==NULL NOT ok in current implementation */
  if(ap.maxLen <= 32)
    pStats32dG(ap.np,pools,precalcScores,f);
  else pStats64dG(ap.np,pools,precalcScores,f);
}
