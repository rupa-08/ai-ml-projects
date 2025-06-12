# Date format: 2000/01/01
# converter.bs_to_ad(date) # BS to AD conversion
# converter.ad_to_bs(date) # AD to BS conversion
 
# logic:
# 1. Get the date from the user -> date
# 2. Get the conversion type from the user -> conversion_type --> using radio
# 3. If conversion_type is 'bs_to_ad', convert the date from BS to AD
# 4. If conversion_type is 'ad_to_bs', convert the date from AD to BS

import streamlit as st
from nepali_date_utils import converter

st.title("Date Converter")

# Sidebar
st.sidebar.header("Select Conversion Type")
conversion_type = st.sidebar.radio("Choose conversion type:", ("BS to AD", "AD to BS"))

date = name = st.sidebar.text_input("Enter Date", "2000/01/01")

btn = st.sidebar.button('Submit')

if btn:
    if conversion_type == "BS to AD":
        try:
            # Convert BS to AD
            converted_date = converter.bs_to_ad(date)
            st.subheader("Your Converted Date is")
            st.success(f"📅  **BS  {date}  =  AD   {converted_date}**")
        except Exception as e:
            st.error("Invalid BS date! Please check the inputs.")

    elif conversion_type == "AD to BS":
        try:
            # Convert AD to BS
            converted_date = converter.ad_to_bs(date)
            st.success(f"📅 **AD {date} = BS {converted_date}**")
        except Exception as e:
            st.error("Invalid AD date! Please check the inputs.")