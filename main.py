import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.subheader("hanieh salehi")
st.write(" private shared google sheet.")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(usecols=[0,1, 2, 3])

st.dataframe(df)

# Print results.
st.write("Use [FOR command] to show data:")

for row in df.itertuples():
    st.write(f"Name : {row.name} , Famil: {row.famil} , Age: {row.age}, city: {row.city}")
