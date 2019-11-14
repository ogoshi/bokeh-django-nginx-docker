from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer(url="https://api.ecmwf.int/v1",key="9d3f4e563ad01ca60184f9792c842476",email="ialmeida.uerj@gmail.com")




server = ECMWFDataServer()    
server.retrieve({
"dataset"    : 'cams_nrealtime',
    "class"      : 'MC',
    "type"       : 'SP',
    "stream"     : 'OPER',
    "expver"     : '0001',
    "levtype"    : 'SFC',
    "param"      : '165.128',
    "time"       : '0000/0600/1200/1800',
    "step"       : '0',
    "resol"      : 'AUTO',
    "grid"       : '0.4/0.4',
    "padding"    : '0',
    "expect"     : 'ANY',
    'format'    : "netcdf",
    "date"       : '20120705/20120706/20120707',
    'target'    : "data.nc"
})
