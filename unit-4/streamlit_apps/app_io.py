import streamlit as st
import pandas as pd
import json

st.title('📂 AI Batch Preprocessor Playground')
st.write('Upload CSV datasets, clean inputs, and export AI summary sheets.')

uploaded_file = st.file_uploader('Choose a CSV input file', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('Raw Data Preview:')
    st.dataframe(df.head(5))
    
    if st.button('Generate AI Preprocessed Output'):
        # Perform simple cleaning
        df_clean = df.copy()
        if 'text' in df_clean.columns:
            df_clean['text'] = df_clean['text'].str.strip().str.upper()
            
        st.subheader('Preprocessed Data Preview:')
        st.dataframe(df_clean.head(5))
        
        # Convert output to csv string for download button
        csv_string = df_clean.to_csv(index=False).encode('utf-8')
        st.download_button(
            label='Download Processed CSV File',
            data=csv_string,
            file_name='ai_processed_outputs.csv',
            mime='text/csv'
        )
