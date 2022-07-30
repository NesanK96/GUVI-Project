import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

# title to our app
st.title('Chennai House Price Predictor')

### gif from local file
file_ = open("valluvar-kottam.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

st.header('**Welcome to Chennai! #NammaOOruNammaGethu**')
st.markdown('')
# @st.cache(suppress_st_warning=True)  


Name = st.text_input("Hello! Welcome here. What's your name?")

AREA = st.selectbox("Select the Area you're looking for:", ["Karapakkam", "Adyar", "Chrompet", "Velachery", "KK Nagar", "Anna Nagar", "T Nagar"])

# AREA:
if (AREA == "Karapakkam"):
	AREA = 0	
	st.write("[KARAPAKKAM's  encyclopedia](https://en.wikipedia.org/wiki/Karapakkam)")

elif (AREA == "Adyar"):
	AREA = 1
	st.write("[ADYAR's	encyclopedia](https://en.wikipedia.org/wiki/Adyar,_Chennai)")

elif (AREA == "Chrompet"):
	AREA = 2
	st.write("[CHROMPET's	encyclopedia](https://en.wikipedia.org/wiki/Chromepet)")

elif (AREA == "Velachery"):
	AREA = 3
	st.write("[VELACHERY's	encyclopedia](https://en.wikipedia.org/wiki/Velachery)")

elif (AREA == "KK Nagar"):
	AREA = 4
	st.write("[KK NAGAR's  encyclopedia](https://en.wikipedia.org/wiki/K._K._Nagar,_Chennai)")

elif (AREA == "Anna Nagar"):
	AREA = 5
	st.write("[ANNA NAGAR's  encyclopedia](https://en.wikipedia.org/wiki/Anna_Nagar)")

elif (AREA == "T Nagar"):
	AREA = 6
	st.write("[T NAGAR's  encyclopedia](https://en.wikipedia.org/wiki/T._Nagar)")
	
INT_SQFT = st.slider("Size of the building required, in sqft:", 500, 2500)
# st.text('Requirement: {}'.format(INT_SQFT))

N_BEDROOM = st.slider("How many Bedrooms needed?", 1, 4)
# st.text('Selected: {}'.format(N_BEDROOM))

N_BATHROOM = st.slider("Bathrooms preference:", 1,2)
# st.text('Selected: {}'.format(N_BATHROOM))

SALE_COND = st.sidebar.selectbox("Sale condition preferred", ["Partial Sale", "Transfer within Family", "AbNormal Sale", "Normal Sale", "Adjacent Land"])

# SALE COND:
if (SALE_COND == "Partial Sale"):
	SALE_COND = 0
elif (SALE_COND == "Transfer within Family"):
	SALE_COND = 1
elif (SALE_COND == "AbNormal Sale"):
	SALE_COND = 2
elif (SALE_COND == "Normal Sale"):
	SALE_COND = 3
elif (SALE_COND == "Adjacent Land"):
		SALE_COND = 4

	
PARK_FACIL = st.sidebar.radio("Parking facility required", {"Yes":1, "No":0})

if PARK_FACIL == "No":
	PARK_FACIL = 0
elif PARK_FACIL == "Yes":
	PARK_FACIL = 1

UTILITY_AVAIL = st.sidebar.selectbox("Facilities Available. Choose you Convenience:", ["Electricity only Available", "Electricity + Gas", 
																					"Electricity + Gas + Water", "All Public facilities available"])

if UTILITY_AVAIL == "Electricity only Available":
	UTILITY_AVAIL = 0
elif UTILITY_AVAIL == "Electricity + Gas":
	UTILITY_AVAIL = 1
elif UTILITY_AVAIL == "Electricity + Gas + Water":
	UTILITY_AVAIL = 2
elif UTILITY_AVAIL == "All Public facilities available":
	UTILITY_AVAIL = 3

	
STREET = st.sidebar.radio("Access to Street:", ["NoAccess", "Paved", "Gravel"])
# st.text('Selected: {}'.format(STREET))
if STREET == "NoAccess":
	STREET = 0
elif STREET == "Paved":
	STREET = 1
elif STREET == "Gravel":
	STREET = 2

MZZONE = st.sidebar.selectbox("Zone preference:", ["Agricultural Zone", "Commercial Zone", "Industrial Zone", "Residential High Density", 
												"Residential Low Density", "Residential Medium Density"])
if MZZONE == "Agricultural Zone":
	MZZONE = 0
elif MZZONE == "Commercial Zone":
	MZZONE = 1
elif MZZONE == "Industrial Zone":
	MZZONE = 2
elif MZZONE == "Residential High Density":
	MZZONE = 3
elif MZZONE == "Residential Low Density":
	MZZONE = 3
elif MZZONE == "Residential Medium Density":
	MZZONE = 3

BUILDTYPE = st.sidebar.radio("Building Use", ["Commercial", "House", "Other_purpose"])
# st.text('Buildtype: {}'.format(BUILDTYPE))

Commercial       = 0
House            = 0
Other_purpose    = 0

# BUILD TYPE 
if BUILDTYPE == "Commercial":
	Commercial 		= 1
	House 	   		= 0
	Other_purpose 	= 0

elif BUILDTYPE == "House":
	Commercial 		= 0
	House 	   		= 1
	Other_purpose 	= 0

elif BUILDTYPE == "Other_purpose":
	Commercial 		= 0
	House 	   		= 0
	Other_purpose 	= 1

AGE_OF_BUILD = st.slider("Required age of building:", 5, 60)
# st.text(f"Age of Building required is : {AGE_OF_BUILD}")


# check if the button is pressed or not
if(st.button('Predict the price')==True):

	# loading XG model pickle
	pickle_in = open('regressor.pkl', 'rb')
	regressor = pickle.load(pickle_in)

	feature_list = [[AREA, INT_SQFT, N_BEDROOM, N_BATHROOM,  SALE_COND, PARK_FACIL, UTILITY_AVAIL, STREET, MZZONE, Commercial, House, Other_purpose, AGE_OF_BUILD]]
	
	# loading scaler pickle:
	pkl_scalar_in = open("scale.pkl", "rb")
	scaler = pickle.load(pkl_scalar_in)

	x = scaler.transform(feature_list)

	single_sample = np.array(x).reshape(1,-1)
	print(single_sample)

	prediction = regressor.predict(single_sample)

	max = int(prediction*1.025)
	min = int(prediction*0.975)

	st.success("Hey {}! The expected price range for your DREAM building is between INR {} and INR {}.".format(Name, min, max))


st.subheader("Check out my profiles:") 
st.caption("Hello! I'm Nesan. Thanks for showing interest in us. Hope you enjoyed being here!")
st.write("	[LinkedIn](https://www.linkedin.com/in/nesan-k-4b1258151/)	| [GitHub](https://github.com/NesanK96)")