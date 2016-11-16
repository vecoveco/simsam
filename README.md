# simsam (SIMple SAMple) 
========================

Simsam (SIMple SAMple) explains complex mathematical and physical prozesses with python.


#### Description
----------------

wip


# Level 1 
===========

Level 1A: Reconstructed, unprocessed instrument data at full resolution, time referenced, and annotated with ancillary information, 
including radiometric and geometric calibration coefficients and georeferencing parameters (i.e., platform ephemeris), computed and appended, 
but not applied, to Level 0 data.

Level 1B: Radiometrically corrected and geolocated Level 1A data that have been processed to sensor units..

Level 1C: Common intercalibrated brightness temperature (Tc) products using the GPM Microwave Imager (GMI) Level 1B as the reference standard.

----------------------------------------------------------
### 1A-GMI: GMI Packet Data Transmitted by the Satellite
----------------------------------------------------------

> 1A.GPM.GMI.COUNT2016.20150609-S000921-E014155.007256.V04A.HDF5

Resolution | Region - Dates  |	Latency  | 	Format   | 	Source  
-----------|------------------|-----------|-----------|----------
4km x 4km - 16 orbits per day| 	Latitudes 70°N-S, March 2014 - present| 	40 hours (Prod)| 	HDF5 |	Prod: FTP (PPS)*(/YYYY/MM/DD/1A)

1AGMI contains unpacked packet data from GMI science data from the GMI passive microwave instrument flown on the GPM satellite. 
Swath S1 has 9 channels which are similar to TRMM TMI (10V 10H 19V 19H 23V 37V 37H 89V 89H). 
Swath S2 has 4 channels similar to AMSU-B (166V 166H 183+/-3V 183+/-8V). Data for both swaths is observed in the same revolution of the instrument. 
Swath S3 has ScienceDataHeader. Swath S4 has full rotation for low freq channels (S1). Swath S5 has full rotation for high freq channels (S2).

-----------------------------------------
### 1B-GMI: GMI brightness temperatures
-----------------------------------------

> B.GPM.GMI.TB2015.20150609-S000921-E014155.007256.V04A.HDF5

The Level 1B algorithm and software transform Level 0 counts into geolocated and calibrated antenna temperatures (Ta) and brightness temperatures (Tb). 
Ta is obtained by utilizing the sensor radiometric calibration as well as various corrections based on after launch analyses. 
Tb is derived from Ta after antenna pattern correction (APC) and along scan corrections. 
Figure 1.16 describes the relationship between algorithm components and products (or output).

Resolution | Region - Dates  |	Latency  | 	Format   | 	Source  
-----------|------------------|-----------|-----------|----------
Varies by Channel - 16 orbits per day |	Latitudes 70°N-S, Past 2 Weeks (NRT) |	20 minutes (NRT); 6 hours (Prod) 	|HDF5 |	FTP (PPS) (/YYYY/MM/DD/1B)

-----------------------------------------
### 1C-GMI: Calibrated GMI brightness temperatures
-----------------------------------------

> 1C.GPM.GMI.XCAL2015-C.20150609-S000921-E014155.007256.V04A.HDF5

The Level 1C algorithms transform equivalent Level 1B radiance data into Level 1C products. The input source data are geolocated and radiometric calibrated antenna temperature (Ta) or brightness temperature (Tb). The output Level 1C products are common intercalibrated brightness temperature (Tc) products using the GPM Microwave Imager (GMI) as the reference standard. The Level 1C algorithms contain the following major components:

    > Orbitization.
    > Satellite intercalibration.
    > Quality control.
    > Ancillary data calculations.

The detail of L1C algorithms and implementation depends on the details of each sensor. In this document, the Level 1C algorithms are described in a general sense. Individual sensor-specific details are provided separately in Appendices A through G: A) GMI, B) LIC-R GMI, C) Tropical Rainfall Measuring Mission (TRMM) Microwave Imager (TMI), D) Special Sensor Microwave Imager/Sounder (SSMI/S), E) Advanced Microwave Scanning Radiometer 2 (AMSR2), F) Advanced Technology Microwave Sounder (ATMS), G) Sondeur Atmospherique du Profil d'Humidite Intertropicale par Radiometrie (SAPHIR), and H) Microwave Humidity Sounder (MHS).

Resolution | Region - Dates  |	Latency  | 	Format   | 	Source  
-----------|------------------|-----------|-----------|----------
Varies by Channel - 16 orbits per day |	orbital, Past 2 Weeks (NRT) |	20 minutes (NRT); 6 hours (Prod) 	|HDF5 |	FTP (PPS) (/YYYY/MM/DD/1C)


# Level 2
===========

Derived geophysical parameters at the same resolution and location as those of the Level 1 data.

### 1C-GMI: Calibrated GMI brightness temperatures
-----------------------------------------

> 1C.GPM.GMI.XCAL2015-C.20150609-S000921-E014155.007256.V04A.HDF5

The Level 1C algorithms transform equivalent Level 1B radiance data into Level 1C products. The input source data are geolocated and radiometric calibrated antenna temperature (Ta) or brightness temperature (Tb). The output Level 1C products are common intercalibrated brightness temperature (Tc) products using the GPM Microwave Imager (GMI) as the reference standard. The Level 1C algorithms contain the following major components:

    > Orbitization.
    > Satellite intercalibration.
    > Quality control.
    > Ancillary data calculations.

The detail of L1C algorithms and implementation depends on the details of each sensor. In this document, the Level 1C algorithms are described in a general sense. Individual sensor-specific details are provided separately in Appendices A through G: A) GMI, B) LIC-R GMI, C) Tropical Rainfall Measuring Mission (TRMM) Microwave Imager (TMI), D) Special Sensor Microwave Imager/Sounder (SSMI/S), E) Advanced Microwave Scanning Radiometer 2 (AMSR2), F) Advanced Technology Microwave Sounder (ATMS), G) Sondeur Atmospherique du Profil d'Humidite Intertropicale par Radiometrie (SAPHIR), and H) Microwave Humidity Sounder (MHS).

Resolution | Region - Dates  |	Latency  | 	Format   | 	Source  
-----------|------------------|-----------|-----------|----------
Varies by Channel - 16 orbits per day |	orbital, Past 2 Weeks (NRT) |	20 minutes (NRT); 6 hours (Prod) 	|HDF5 |	FTP (PPS) (/YYYY/MM/DD/1C)


# GPM Public Data
==================

/gpmdata contains the latest version of available data products. 

Directories are laid out as:

/gpmdata/documents ****!!!! Please review the contents of 
                       this directory. It contains important 
                       data notices and caveats !!!!****
/gpmdata/geolocation  contains geolocation related files
/gpmdata/coincidence contains satellite-ground coincidence information
/gpmdata/browse contains PNG browse images of products.

Data products exist under:
> /gpmdata/YYYY/MM/DD/

  base/reg  - 1B base radiometer products
  1B    - 1B radiometer products for GPMcore and all partners
  1C    - 1C radiometer products for GPMcore and all partners
  radar - L2 and L3 products from DPR and Combined
  gprof - L2 and L3 products from GPROF for GPMcore and all partners
  imerg - IMERG products
