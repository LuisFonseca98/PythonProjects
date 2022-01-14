import cv2
#----------Deteção de pixeis ativos----------#
cap = cv2.VideoCapture('cam.mov')
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
        
	diff = cv2.absdiff(frame1, frame2)
#----------Melhoramento da Imagem----------#	
	gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
	gray = cv2.resize(gray,None,fx=0.8,fy=0.8,interpolation = cv2.INTER_LINEAR)
	frame1 = cv2.resize(frame1,None,fx=0.8,fy=0.8,interpolation = cv2.INTER_LINEAR)
	blur = cv2.medianBlur(gray, 5)
	_, thresh = cv2.threshold(blur, 10, 255,cv2.THRESH_BINARY)
	dilated = cv2.dilate(thresh, None, iterations=7)
	cv2.imshow("as", dilated)
	
#----------Extração dos componentes----------#
	contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for contour in contours:
		if cv2.contourArea(contour) < 700:
			continue

#----------Identificação e classificação dos componentes----------#
		x, y, w, h = cv2.boundingRect(contour)
		largura = x+w
		altura = y+h
		#recorrendo ás proporcões humanas, aproximadamente
		#a largura é cerca de 1/4 da altura
		#portanto aumentando ligeiramente o valor da largura
		# obtemos resultados mais coerentes
		if(h>w*1.30):
			#pessoa
			cv2.rectangle(frame1, (x, y), (largura,altura), (255, 0, 0), 2)
			cv2.putText(frame1, "Pessoa" ,(x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),)
			
		elif(h<=w):
			#carro
			cv2.rectangle(frame1, (x, y), (largura,altura), (0, 255, 0), 2)
			cv2.putText(frame1, "Carro" ,(x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),)
		else:
			cv2.rectangle(frame1, (x, y), (largura,altura), (0, 0, 255), 2)
			cv2.putText(frame1, "Outro", (x, y), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255),)

#----------Visualização de Resultados----------#
	cv2.imshow("feed", frame1)
	frame1 = frame2
	ret, frame2 = cap.read()
	if not ret:
		break
	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()
