import _mysql as mysql

db=mysql.connect("localhost","u413",open("/var/u413.pwd","r").read().rstrip('\r\n'))

#wrap the ugly _mysql interface with a nice function
#returns a list of dictionaries corresponding to the rows and columns
def query(q):
	db.query(q)
	r=db.store_result()
	#format result
	fr=[]
	row=(0,)
	while True:
		row=r.fetch_row(how=1)
		if row!=():
			fr.append(row[0])
		else:
			break
	return fr