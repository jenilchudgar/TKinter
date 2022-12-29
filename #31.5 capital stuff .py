# def state_capitals():
#     root.geometry("500x300")
#     # Hide All Previous Frames
#     hideAllFrames()
#     state_capitals_frame.pack(fill=BOTH,expand=1)

#     global isFirstTime
#     if isFirstTime:
#         global states
#         states = sorted([e.replace(".png","") for e in os.listdir("states")])

#     if len(states) >=1:
#         capitals = {}
#         c = [
#             'Hyderabad','Itanagar','Dispur','Patna','Raipur','Panaji','Gandhinagar','Chandigarh','Shimla','Ranchi','Bengaluru','Thiruvanathapuram','Bhopal','Mumbai','Imphal','Shillong','Aizawal','Kohima','Bhubneswar','Chandigarh','Jaipur','Gangtok','Chennai','Hyderabad','Agartala','Dehradun','Lucknow','Kolkata'
#         ]
#         top1 = [
#             'Visakhapatnam','Tawang','Guwahati','Bhagalpur','Bhilai','Taluka','Ahmedabad','Faridabad','Dharamsala','Jamshedpur','Kalaburagi','Kozhikode','Gwalior','Pune','Thoubal','Tura','Champhai','Soma','Cuttack','Ludhiana','Jodhpur','Rangpo','Coimbatore','Warangal','Kailasahar','Haridwar','Agra','Siliguri'
#         ]
#         top2 = [
#             'Vijayawada','East Kameng','Dibrugarh','Muzaffarpur','Bilaspur','New Goa City','Surat','Gurugram','Solan','Dhanbad','Manglore','Kochi','Indore','Nasik','East Fhalna','Umlyngka','Lunglei','Dimapur','Raurkela','Amritsar','Kota','Nayabazar',
#             'Madurai','Nizamabad','	Udaipur','Rudrapur','	Kanpur','Durgapur'
#         ]
#         print(len(c),len(top1),len(top2))
#         capitals = {}
#         i = 0
#         for e in states:
#             l = [c[i].lower().replace("\t","")]
#             l.append(top1[i].lower().replace("\t",""))
#             l.append(top2[i].lower().replace("\t",""))
#             capitals[e] = l
#             i+=1

#         answer_list = []
#         randNo = randint(0,len(states)-1)
#         state = states[randNo]
#         options = capitals[state]
#         answer = options[0]
#         shuffle(options)

#         state_label = Label(state_capitals_frame,text=f"State: {state.title().replace('_',' ')}",font=('Calibri',18),anchor=CENTER)
#         state_label.pack()

#         global capital_var
#         capital_var = IntVar()

#         # Create Radio Buttons
#         capital_radio_btn1 = Radiobutton(state_capitals_frame,text=options[0].title(),variable=capital_var,value=1,font=('Calibri',15),justify=LEFT)
#         capital_radio_btn1.pack()

#         capital_radio_btn2 = Radiobutton(state_capitals_frame,text=options[1].title(),variable=capital_var,value=2,font=('Calibri',15),justify=LEFT)
#         capital_radio_btn2.pack()

#         capital_radio_btn3 = Radiobutton(state_capitals_frame,text=options[2].title(),variable=capital_var,value=3,font=('Calibri',15),justify=LEFT)
#         capital_radio_btn3.pack()

#         btn = Button(state_capitals_frame,text="Pass",command=state_capitals,font=('Calibri',16))
#         btn.pack(pady=10,padx=10)

#         isFirstTime = False
#     else:
#         Label(state_capitals_frame,text="Game Over!",font=('Calibri',50),fg="blue").pack()
#         return

#     # Remove this state
#     states.remove(state)
