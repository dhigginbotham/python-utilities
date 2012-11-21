#def getCsv(file,type,col):
#    import csv, re
#    column_names = csv.reader(open(file, encoding='utf8'), dialect='excel-tab')
#    lcn = list(column_names)
#    reader = csv.DictReader(open(file,'r'), lcn[0], dialect='excel', delimiter='\t')
#    totalrows = 0
#    for row in reader:
#      totalrows += 1
#      if row['ClassName'] == type:
#          selection = row[col]
#          return (selection)

#def getFields(file,type,col):
#    import csv, re
#    columns = csv.reader(open(file, encoding='utf-8'), dialect='excel-tab')
#    col_list = list(columns)
#    col_len = len(col_list)
#    print (col_list[0])
#    rows = csv.DictReader(open(file,'r'), col_list[0], dialect='excel', delimiter='\t')
#
#    for cols in rows, col:
#        if cols['ClassName'] == type:
#            xy = r[col]
#            return (xy)

def makeHtml(dir,file,type):
    import os, csv, re
    prefix= "D:\\MLSData\\"
    predir= dir
    suffix= "\\_python\\html\\"
    
    if not os.path.exists(prefix):
        os.makedirs(prefix + predir + suffix)
    
#    file = open(dir + 'myfile.dat', 'w+')
    
    header= """<!DOCTYPE html >\r\n
    <html>\r\n
    \t<head>\r\n
    \t\t<title>Income Property</title>\r\n
    \t\t<script type="text/javascript" src="pholder_dan_dav_mod.js?Ver=2.0"></script>\r\n
    \t\t<link rel="stylesheet" href="css/style.css?Ver=2.0" type="text/css" />\r\n
    \t\t<!-- add mobile stuff -->\r\n
    \t\t<meta name="HandheldFriendly" content="True">\r\n
    \t\t<meta name="MobileOptimized" content="320">\r\n
    \t\t<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\r\n
    \t</head>\r\n
    \t<body>\r\n
    """
    
    footer= """\t</body>\r\n
    </html>
    """
    ul_open= '\t\t<ul id="feed" class="media list clearfix">\r\n'
    ul_close= '\t\t</ul>\r\n'
    
    li_open= '\t\t\t<li class="clearfix header-child"><div class="twocol first"><label>'
    li_middle= ': </label></div><div class="tencol last">&nbsp; {P.'
    li_close= '}</div></li>\r\n'
    
    column_names = csv.reader(open(file, 'r', encoding='utf8'), dialect='excel-tab')
    lcn = list(column_names)
    reader = csv.DictReader(open(file,'r'), lcn[0], dialect='excel', delimiter='\t')
    totalrows = 0

    long,sys = set(),set()
    for row in reader:
      totalrows += 1
      if row['ClassName'] == type:
          long= (row['LongName'])
          sys= (row['SystemName'])
    
    print (header)
    print (ul_open)
    i= 0
    for rows in sys:
        i += 1
        print (li_open + (long) + li_middle + (sys) + li_close)
    
    print (ul_close)
    print(footer)


makeHtml('SPO', 'D:\MLSData\SPO\MetadataTables_SPO.txt', 'RS_1')