from flask import Flask,render_template,request

app=Flask(__name__) #application

def findGrade(mark):

	if(mark<35):
		return 'F'
	elif(mark<45):
		return 'S'
	elif(mark<65):
		return 'C'
	elif(mark<75):
		return 'B'
	else:
		return 'A'

@app.route('/')
def index():

	return render_template('fill_details.html')

@app.route('/getresults',methods=['POST'])
def getresults():

	details=request.form
	
	name=details['nm']
	ID=details['id']
	maths=float(details['maths'])
	phy=float(details['phys'])
	chem=float(details['chem'])

	avg=round((maths+chem+phy)/3.0)
	mathsGrade=findGrade(maths)
	phyGrade=findGrade(phy)
	chemGrade=findGrade(chem)

	resultDict={"name":name,"avg":avg,"mgrade":mathsGrade,"pgrade":phyGrade,"cgrade":chemGrade}

	return render_template('student_result.html',results=resultDict)

app.run(debug=True)