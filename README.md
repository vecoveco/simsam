# simsam (SIMple SAMple) 
========================

Simsam (SIMple SAMple) explains complex mathematical and physical prozesses with python.


#### Description
----------------

wip


# Level 1 
----------

Level 1A: Reconstructed, unprocessed instrument data at full resolution, time referenced, and annotated with ancillary information, 
including radiometric and geometric calibration coefficients and georeferencing parameters (i.e., platform ephemeris), computed and appended, 
but not applied, to Level 0 data.

Level 1B: Radiometrically corrected and geolocated Level 1A data that have been processed to sensor units..

Level 1C: Common intercalibrated brightness temperature (Tc) products using the GPM Microwave Imager (GMI) Level 1B as the reference standard.

### 1A-GMI: GMI Packet Data Transmitted by the Satellite

Resolution    	Region - Dates    	Latency    	Format    	Source    	DL   
4km x 4km - 16 orbits per day 	Latitudes 70°N-S, March 2014 - present 	40 hours (Prod) 	
HDF5 	Prod: FTP (PPS)*

(/YYYY/MM/DD/1A)

1AGMI contains unpacked packet data from GMI science data from the GMI passive microwave instrument flown on the GPM satellite. 
Swath S1 has 9 channels which are similar to TRMM TMI (10V 10H 19V 19H 23V 37V 37H 89V 89H). 
Swath S2 has 4 channels similar to AMSU-B (166V 166H 183+/-3V 183+/-8V). Data for both swaths is observed in the same revolution of the instrument. 
Swath S3 has ScienceDataHeader. Swath S4 has full rotation for low freq channels (S1). Swath S5 has full rotation for high freq channels (S2).


### 1B-GMI: GMI brightness temperatures


The Level 1B algorithm and software transform Level 0 counts into geolocated and calibrated antenna temperatures (Ta) and brightness temperatures (Tb). 
Ta is obtained by utilizing the sensor radiometric calibration as well as various corrections based on after launch analyses. 
Tb is derived from Ta after antenna pattern correction (APC) and along scan corrections. 
Figure 1.16 describes the relationship between algorithm components and products (or output).
