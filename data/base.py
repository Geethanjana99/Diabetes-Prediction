st_style = """           /* Sidebar styling */
           .css-1d391kg {
               background-color: white !important;
               border-right: 2px solid #3b82f6 !important;
           }
           
           /* Sidebar container */
           .css-1lcbmhc {
               background-color: white !important;
           }
           
           /* Sidebar content area */
           .css-17eq0hr {
               background-color: white !important;
           }        <style>
           #MainMenu {visibility: hidden;}
           footer {visibility: hidden;}
           header {visibility: hidden;}
           div.block-container {padding-top:1rem;}
           .css-ysnqb2 e1g8pov64 {margin-top: -75px;}
           
           /* Global theme styling */
           .stApp {
               background-color: white !important;
               color: #1f2937 !important;
           }
           
           /* Sidebar styling */
           .css-1d391kg {
               background-color: #ffffff !important;
               border-right: 2px solid #3b82f6 !important;
           }
           
           /* Sidebar text styling */
           .stSidebar .stMarkdown, .stSidebar .stText, .stSidebar p, .stSidebar div, .stSidebar span, .stSidebar label {
               color: #000000 !important;
               font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
           }
           
           /* Comprehensive sidebar white background */
           .stSidebar {
               background-color: white !important;
           }
           
           .stSidebar > div {
               background-color: white !important;
           }
           
           .stSidebar .stMarkdown {
               background-color: white !important;
           }
           
           /* Sidebar input containers */
           .stSidebar .stNumberInput > div {
               background-color: white !important;
           }
           
           .stSidebar .stSelectbox > div {
               background-color: white !important;
           }
           
           /* Sidebar input labels */
           .stSidebar .stNumberInput label, .stSidebar .stSelectbox label {
               color: #000000 !important;
               font-weight: 500 !important;
           }
           
           /* Text and content styling */
           .stMarkdown, .stText, p, div, span {
               color: #1f2937 !important;
               font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
           }
           
           /* Headers styling */
           h1, h2, h3, h4, h5, h6 {
               color: #1f2937 !important;
               font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
           }
           
           /* Button styling */
           .stButton button {
               background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
               color: white !important;
               border: none !important;
               border-radius: 8px !important;
               font-weight: 500 !important;
               font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
           }
           
           .stButton button:hover {
               background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%) !important;
               transform: translateY(-1px) !important;
               box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
           }
           
           /* Input field styling */
           .stNumberInput input, .stSelectbox select, .stSlider {
               background-color: white !important;
               color: #000000 !important;
               border: 2px solid #e5e7eb !important;
               border-radius: 8px !important;
               font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
           }
           
           .stNumberInput input:focus, .stSelectbox select:focus {
               border-color: #3b82f6 !important;
               box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
               color: #000000 !important;
           }
           
           /* Sidebar specific input styling */
           .stSidebar .stNumberInput input {
               color: #000000 !important;
               background-color: white !important;
           }
           
           /* Metric styling */
           .metric-container {
               background: white !important;
               border: 2px solid #e5e7eb !important;
               border-radius: 12px !important;
               padding: 16px !important;
               box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
           }
           
           /* Chart styling */
           .stPlotlyChart {
               background-color: white !important;
               border-radius: 12px !important;
               border: 2px solid #e5e7eb !important;
               box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
           }
           
           /* Expander styling */
           .streamlit-expanderHeader {
               background-color: #f8fafc !important;
               color: #1f2937 !important;
               border: 2px solid #3b82f6 !important;
               border-radius: 8px !important;
               font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
           }
           
           .streamlit-expanderContent {
               background-color: white !important;
               border: 2px solid #e5e7eb !important;
               border-top: none !important;
               border-radius: 0 0 8px 8px !important;
           }
           
           /* Success/error message styling */
           .stSuccess {
               background-color: #f0f9ff !important;
               color: #1f2937 !important;
               border-left: 4px solid #3b82f6 !important;
           }
           
           .stError {
               background-color: #fef2f2 !important;
               color: #1f2937 !important;
               border-left: 4px solid #ef4444 !important;
           }
           
           .stWarning {
               background-color: #fffbeb !important;
               color: #1f2937 !important;
               border-left: 4px solid #f59e0b !important;
           }
           
           /* Tab styling */
           .stTabs [data-baseweb="tab-list"] {
               background-color: #f8fafc !important;
               border-radius: 8px !important;
               border: 2px solid #e5e7eb !important;
           }
           
           .stTabs [data-baseweb="tab"] {
               color: #1f2937 !important;
               font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
           }
           
           .stTabs [aria-selected="true"] {
               background-color: #3b82f6 !important;
               color: white !important;
           }
           </style>
           """

footer = """
    <style>
    .footer {
        position: relative;
        left: 0;
        width: 100%;
        background: white;
        text-align: center;
        padding: 16px;
        font-size: 14px;
        color: #1f2937;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.1);
        border-top: 2px solid #3b82f6;
        margin-top: 40px;
    }
    .footer-brand {
        display: inline-flex;
        align-items: center;
        margin-bottom: 8px;
    }
    .footer-heart {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border-radius: 6px;
        padding: 4px;
        margin-right: 8px;
        font-size: 12px;
    }
    .footer-title {
        font-weight: bold;
        color: #1f2937;
        margin: 0 8px 0 0;
    }
    .footer-subtitle {
        color: #3b82f6;
        font-size: 12px;
        font-weight: 500;
    }
    .footer-divider {
        border-top: 1px solid #e5e7eb;
        margin: 12px 0 8px 0;
        padding-top: 8px;
    }
    .footer-description {
        color: #4b5563;
        margin-bottom: 8px;
    }
    </style>
    <div class="footer">
        <div class="footer-brand">
            <div class="footer-heart">❤️</div>
            <span class="footer-title">CareSync</span>
            <span class="footer-subtitle">Healthcare Management</span>
        </div>
        <div class="footer-description">
            Professional Diabetes Risk Assessment | Clinical Decision Support System
        </div>
        <div class="footer-divider">
            © 2025 CareSync Healthcare Management System. All rights reserved.
        </div>
    </div>
    """


head = """
    <div style="display: flex; 
    justify-content: center; 
    align-items: center; 
    margin-bottom: 20px; 
    padding: 20px;
    background: white;
    border-bottom: 2px solid #3b82f6;">
        <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); 
        color: white; 
        border-radius: 12px; 
        padding: 8px; 
        margin-right: 12px;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);">
            ❤️
        </div>
        <div>
            <h1 style="font-size: 36px; 
            font-weight: bold; 
            color: #1f2937; 
            margin: 0; 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
                CareSync
            </h1>
            <p style="font-size: 14px; 
            color: #3b82f6; 
            margin: 0; 
            font-weight: 500;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
                Diabetes Risk Assessment
            </p>
        </div>
    </div>
    <div style="text-align: center; 
    font-size: 18px; 
    color: #1f2937; 
    margin-bottom: 40px; 
    padding: 20px;
    background: white;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
        Professional AI-powered diabetes risk assessment and clinical decision support platform
    </div>
    """

mrk = """
<div style="background: white; 
color: #1f2937; 
margin-bottom: 50px;
padding: 20px;
max-width: 300px;
text-align: center;
border-radius: 12px; 
border: 2px solid {};
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
    <div style="color: {}; font-weight: bold; margin-bottom: 8px;">
        {}
    </div>
</div>
"""


about_diabets = """
## What is diabetes?

**Diabetes** is a chronic health condition that affects how your body turns food into energy. It is characterized by high levels of glucose (sugar) in the blood, which occurs because the body either doesn’t produce enough insulin, doesn’t use insulin effectively, or both.

### **Types of Diabetes**:
1. **Type 1 Diabetes**:
   - An autoimmune condition where the immune system attacks and destroys insulin-producing cells in the pancreas.
   - Typically diagnosed in children and young adults.
   - Requires daily insulin injections to manage blood sugar.

2. **Type 2 Diabetes**:
   - The body becomes resistant to insulin, or the pancreas doesn’t produce enough insulin.
   - Often linked to lifestyle factors like obesity, physical inactivity, and poor diet, but genetics also play a role.
   - Managed through lifestyle changes, medications, and sometimes insulin.

3. **Gestational Diabetes**:
   - Occurs during pregnancy when the body cannot make enough insulin to support the increased demand.
   - Usually resolves after childbirth, but it increases the risk of developing type 2 diabetes later in life.

### **Symptoms of Diabetes**:
- Frequent urination
- Excessive thirst
- Extreme hunger
- Fatigue
- Blurred vision
- Slow-healing wounds
- Unexplained weight loss (especially in type 1 diabetes)

### **Complications of Untreated Diabetes**:
- Heart disease
- Kidney damage
- Vision loss (diabetic retinopathy)
- Nerve damage (diabetic neuropathy)
- Increased risk of infections

### **Management**:
- **Diet**: Eating a balanced diet, avoiding high-sugar foods.
- **Exercise**: Regular physical activity to improve insulin sensitivity.
- **Medications**: Insulin therapy or oral diabetes medications.
- **Monitoring**: Regularly checking blood glucose levels.
"""


warn = """
**Important Medical Disclaimer:** This AI-powered assessment tool is designed for educational and informational purposes only. 
The predictions and recommendations provided should not replace professional medical advice, diagnosis, or treatment. 
Please consult with qualified healthcare professionals for comprehensive medical evaluation and personalized treatment plans. 
CareSync Healthcare Management System emphasizes the importance of professional medical supervision for all health-related decisions.
"""