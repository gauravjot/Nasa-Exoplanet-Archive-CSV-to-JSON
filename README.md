# NASA Exoplanet Archive CSV to JSON Parser

This short script opens up a CSV file and converts it into JSON. 

The latest version of CSV file used can be downloaded from [https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=planets](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=planets)

Another CSV for Exoplanet archive can be found at [https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS)

Before someone suggests using `csv` python module, it is written without it purposefully to incorporate RegEx usage instead.