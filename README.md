# simsam (SIMple SAMple) 
========================

Simsam (SIMple SAMple) explains complex mathematical and physical prozesses with python.


#### Description
----------------

wip



# GPM Public Data
==================

/gpmdata contains the latest version of available data products. 

Directories are laid out as:

*/gpmdata/documents* ****!!!! Please review the contents of 
                       this directory. It contains important 
                       data notices and caveats !!!!****
                       
                       
*/gpmdata/geolocation*  
> contains geolocation related files

*/gpmdata/coincidence* 
> contains satellite-ground coincidence information

*/gpmdata/browse* 
> contains PNG browse images of products.

Data products exist under:
*/gpmdata/YYYY/MM/DD/*

 > base/reg  - 1B base radiometer products
 
 > 1B    - 1B radiometer products for GPMcore and all partners
 
 > 1C    - 1C radiometer products for GPMcore and all partners
 
 > radar - L2 and L3 products from DPR and Combined
 
 > gprof - L2 and L3 products from GPROF for GPMcore and all partners
 
 > imerg - IMERG products
 
 
 ----------------------------------------------------------
### 1A
----------------------------------------------------------

> 1A.GPM.GMI.COUNT2016.20150609-S000921-E014155.007256.V04A.HDF5

> 1A-GMI: GMI Packet Data Transmitted by the Satellite

> Level 1A: Reconstructed, unprocessed instrument data at full resolution, time referenced, and annotated with ancillary information, including radiometric and geometric calibration coefficients and georeferencing parameters (i.e., platform ephemeris), computed and appended, but not applied, to Level 0 data.

esolution | Region - Dates  |	Latency  | 	Format   | 	Source  
-----------|------------------|-----------|-----------|----------
4km x 4km - 16 orbits per day| 	Latitudes 70°N-S, March 2014 - present| 	40 hours (Prod)| 	HDF5 |	Prod: FTP (PPS)*(/YYYY/MM/DD/1A)

----------------------------------------------------------
### 1B
----------------------------------------------------------

> 1B.GPM.GMI.TB2015.20150609-S000921-E014155.007256.V04A.HDF5

> 1B-GMI: GMI brightness temperatures

> The Level 1B algorithm and software transform Level 0 counts into geolocated and calibrated antenna temperatures (Ta) and brightness temperatures (Tb). Ta is obtained by utilizing the sensor radiometric calibration as well as various corrections based on after launch analyses. Tb is derived from Ta after antenna pattern correction (APC) and along scan corrections. Figure 1.16 describes the relationship between algorithm components and products (or output). 

Resolution | Region - Dates  |	Latency  | 	Format   | 	Source  
-----------|------------------|-----------|-----------|----------
Varies by Channel - 16 orbits per day |	Latitudes 70°N-S, Past 2 Weeks (NRT) |	20 minutes (NRT); 6 hours (Prod) 	|HDF5 |	FTP (PPS) (/YYYY/MM/DD/1B)


----------------------------------------------------------
### 1C
----------------------------------------------------------

> 1C.GPM.GMI.XCAL2015-C.20150609-S000921-E014155.007256.V04A.HDF5

> 1C-GMI: Calibrated GMI brightness temperatures

> The Level 1C algorithms transform equivalent Level 1B radiance data into Level 1C products. The input source data are geolocated and radiometric calibrated antenna temperature (Ta) or brightness temperature (Tb). The output Level 1C products are common intercalibrated brightness temperature (Tc) products using the GPM Microwave Imager (GMI) as the reference standard. The Level 1C algorithms contain the following major components:

    Orbitization.
    Satellite intercalibration.
    Quality control.
    Ancillary data calculations.

The detail of L1C algorithms and implementation depends on the details of each sensor. In this document, the Level 1C algorithms are described in a general sense. Individual sensor-specific details are provided separately in Appendices A through G: A) GMI, B) LIC-R GMI, C) Tropical Rainfall Measuring Mission (TRMM) Microwave Imager (TMI), D) Special Sensor Microwave Imager/Sounder (SSMI/S), E) Advanced Microwave Scanning Radiometer 2 (AMSR2), F) Advanced Technology Microwave Sounder (ATMS), G) Sondeur Atmospherique du Profil d'Humidite Intertropicale par Radiometrie (SAPHIR), and H) Microwave Humidity Sounder (MHS).

Resolution | Region - Dates  |	Latency  | 	Format   | 	Source  
-----------|------------------|-----------|-----------|----------
Varies by Channel - 16 orbits per day |	orbital, Past 2 Weeks (NRT) |	20 minutes (NRT); 6 hours (Prod) 	|HDF5 |	FTP (PPS) (/YYYY/MM/DD/1C)

----------------------------------------------------------
### gprof
----------------------------------------------------------

> 2A.GPM.GMI.GPROF2014v2-0.20150609-S000921-E014155.007256.V04A.HDF5

> 2A-GPROF-GMI: GMI single-orbit rainfall estimates

> The 2AGPROF (also known as, GPM GPROF (Level 2)) algorithm retrieves consistent precipitation and related science fields from the following GMI and partner passive microwave sensors: GMI, SSMI (DMSP F15), SSMIS (DMSP F16, F17, F18) AMSR2 (GCOM-W1), TMI MHS (NOAA 18&19, METOP A&B), ATMS (NPP), SAPHIR (MT1) This provides the bulk of the 3-hour coverage achieved by GPM. For each sensor, there are near-realtime (NRT) products, standard products, and climate products. These differ only in the amount of data that are available within 3 hours, 48 hours, and 3 months of collection, as well as the ancillary data used. 

Resolution | Region - Dates  |	Latency  | 	Format   | 	Source  
-----------|------------------|-----------|-----------|----------
4km x 4km, 16 orbits per day |	Latitudes 90°N-S, Past 2 weeks (NRT); March 2014 - present (Prod) |	2 hours (NRT); 40 hours (Prod)	|HDF5 |	FTP (PPS) (/YYYY/MM/DD/2A.GPM.GMI)

----------------------------------------------------------
### imerg
----------------------------------------------------------

> 3B-HHR.MS.MRG.3IMERG.20150609-S000000-E002959.0000.V03D.HDF5

> IMERG: Rainfall estimates combining data from all passive-microwave instruments in the GPM Constellation

> This algorithm is intended to intercalibrate, merge, and interpolate “all” satellite microwave precipitation estimates, together with microwave-calibrated infrared (IR) satellite estimates, precipitation gauge analyses, and potentially other precipitation estimators at fine time and space scales for the TRMM and GPM eras over the entire globe. The system is run several times for each observation time, first giving a quick estimate and successively providing better estimates as more data arrive. The final step uses monthly gauge data to create research-level products.

Resolution | Region - Dates  |	Latency  | 	Format   | 	Source  
-----------|------------------|-----------|-----------|----------
0.1° - 30 minute|	Gridded, 60°N-60°S, March 2014 to present |	4 months (Prod / final run)	|HDF5 |	FTP (PPS) (/YYYY/MM/DD/3B.HHR.)

----------------------------------------------------------
### radar
----------------------------------------------------------

> 2A.GPM.DPR.GPM-SLH.20150609-S000921-E014155.007256.V04A.HDF5

> 2A.GPM.DPR.V6-20160118.20150609-S000921-E014155.007256.V04A.HDF5

> 2B.GPM.DPRGMI.2HCSHv2-1.20150609-S000921-E014155.007256.V04A.HDF5

> 2A.GPM.Ka.V6-20160118.20150609-S000921-E014155.007256.V04A.HDF5

> 2A.GPM.Ku.V6-20160118.20150609-S014156-E031430.007257.V04A.HDF5

----------------------------------------------------------
### base
----------------------------------------------------------

