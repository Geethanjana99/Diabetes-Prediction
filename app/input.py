import streamlit as st
import pandas as pd


def app():
    # Minimal CareSync branded header
    st.sidebar.markdown("""
        <div style="background: white; 
        padding: 20px; 
        border-radius: 8px; 
        border: 1px solid #e5e7eb; 
        margin-bottom: 24px;
        text-align: center;">
            <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 8px;">
                <div style="background: #3b82f6; 
                color: white; 
                border-radius: 6px; 
                padding: 4px 8px; 
                margin-right: 8px;
                font-size: 14px;">
                    ❤️
                </div>
                <h3 style="color: #000000; margin: 0; font-size: 18px; font-weight: 600;">
                    CareSync
                </h3>
            </div>
            <p style="color: #000000; font-size: 12px; margin: 0; font-weight: 500;">
                Clinical Assessment Portal
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Clean parameter input section
    st.sidebar.markdown('<p style="color: #000000; font-weight: 600; font-size: 16px; margin-bottom: 8px;">Clinical Parameters</p>', unsafe_allow_html=True)
    st.sidebar.markdown("---")

    # Pregnancies
    pregnancies_value = st.sidebar.number_input(
        'Pregnancies',
        min_value=0,
        max_value=20,
        value=1,
        help="Number of pregnancies"
    )

    # Glucose
    glucose_value = st.sidebar.number_input(
        'Glucose (mg/dL)',
        min_value=0,
        max_value=250,
        value=100,
        help="Plasma glucose concentration"
    )

    # Insulin
    insulin_value = st.sidebar.number_input(
        'Insulin (μU/mL)',
        min_value=0,
        max_value=1000,
        value=100,
        help="2-Hour serum insulin"
    )

    # BMI
    bmi_value = st.sidebar.number_input(
        'BMI',
        min_value=0.0,
        max_value=100.0,
        value=37.0,
        format="%.1f",
        help="Body Mass Index"
    )

    # Age
    age_value = st.sidebar.number_input(
        'Age (years)',
        min_value=0,
        max_value=100,
        value=25,
        help="Patient age"
    )

    # Professional divider
    st.sidebar.markdown("---")
    
    # Minimal reference ranges with better contrast
    st.sidebar.markdown("""
        <div style="background: #f8fafc; 
        padding: 12px; 
        border-radius: 6px; 
        border-left: 3px solid #3b82f6;">
            <p style="color: #000000; font-size: 12px; margin: 0; font-weight: 600;">Reference Ranges</p>
            <p style="color: #000000; font-size: 11px; margin: 4px 0 0 0;">
                Glucose: 70-100 mg/dL • BMI: 18.5-24.9 • Normal ranges for clinical reference
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Minimal disclaimer with better contrast
    st.sidebar.markdown("""
        <div style="background: #fef2f2; 
        padding: 8px; 
        border-radius: 6px; 
        border-left: 3px solid #ef4444; 
        margin: 12px 0;">
            <p style="color: #000000; font-size: 10px; margin: 0;">
                <strong>Medical Disclaimer:</strong> For educational purposes. Consult healthcare professionals for medical advice.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    return pd.DataFrame([[pregnancies_value, glucose_value, insulin_value, bmi_value, age_value]], 
                        columns=['Pregnancies', 'Glucose', 'Insulin','BMI','Age'])    