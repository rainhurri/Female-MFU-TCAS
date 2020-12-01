import streamlit as st
import pandas as pd
import pickle

st.write("""# Classification(KNN) """)
st.write("""## Please answer the following questions. """)

st.sidebar.header('User Input')
st.sidebar.subheader('Please enter your data:')



def get_input():
    #widgets
    v_FacultyID = st.sidebar.radio('School of ...',['School of Agro-industry','School of Cosmetic Science','School of Dentistry','School of Information Technology','School of Integrative Medicine''School of Law','School of Liberal Arts','School of Management','School of Nursing','School of Medicine','School of Science','School of Sinology','School of Social Innovation',])
    v_DepartmentCode = st.sidebar.selectbox('Select your major',['Accounting','Applied Chemistry','Applied Thai Traditional Medicine','Aviation Business Management','Biotechnology','Business Administration','Business Chinese','Chinese Language and Culture','Chinese Study','Computer Engineering','Computer Science and Innovation','Cosmetic Science','Dentistry','Economics','English','Environmental Health','Food Science and Technology','Hospitality Industry Management','Information Technology','International Development','Laws','Logistics and Supply Chain Management','Materials Engineering','Medicine','Multimedia Technology and Animation','Nursing Science','Occupational Health and Safety','Physical Therapy','Posthavest Technology and Logistics','Public Health','Software Engineering','Sports and Health Science','Teaching Chinese Language (5 Year)','Tourism Management','Traditional Chinese'])
    v_TCAS = st.sidebar.radio('TCAS', ['1', '2', '5'])
    v_EntryTypeID = st.sidebar.selectbox('Entry Type', ['Direct admission','Direct admission by school', 'Quota 17 northern provinces','Quota by school','Special for good student',])
    v_HomeRegion = st.sidebar.radio('Home Region be in ...', ['North', 'Not North'])
    v_SchoolRegion = st.sidebar.radio('SchoolRegion be in ...', ['North', 'Not North'])
    v_EntryGPA = st.sidebar.slider('EntryGPA', 1.72, 4.00, 3.25)
    v_GPAX = st.sidebar.slider('GPAX', 1.53, 4.00, 3.32)
    v_GPA_Eng = st.sidebar.slider('GPA_Eng', 1.00, 4.00, 3.42)
    v_GPA_Math = st.sidebar.slider('GPA_Math', 0.72, 4.00, 2.83)
    v_GPA_Sci = st.sidebar.slider('GPA_Sci', 1.00, 4.00, 3.09)
    v_GPA_Sco = st.sidebar.slider('GPA_Sco', 0.70, 4.00, 3.60)
    st.write("""Expectation for studying in MFU:""")
    v_Q1 = st.radio('Beautiful scenary and atmosphere', ['Yes', 'No'])
    v_Q3 = st.radio('Campus and facilities', ['Yes', 'No'])
    v_Q4 = st.radio('Modern and ready-to-use learning support and facilities', ['Yes', 'No'])
    v_Q5 = st.radio('Sources of student scholarship', ['Yes', 'No'])
    v_Q6 = st.radio('Demand by workforce market', ['Yes', 'No'])
    st.write("""Source of information for this application:""")
    v_Q8 = st.radio('Facebook Admission@MFU', ['Yes', 'No'])
    v_Q9 = st.radio('Facebook MFU', ['Yes', 'No'])
    v_Q12 = st.radio('Family/friend/relative', ['Yes', 'No'])
    v_Q13 = st.radio('school teachers', ['Yes', 'No'])
    v_Q19 = st.radio('https://admission.mfu.ac.th', ['Yes', 'No'])
    v_Q20 = st.radio('https://www.mfu.ac.th', ['Yes', 'No'])
    v_Q21 = st.radio('other educational website', ['Yes', 'No'])
    st.write("""Factor to apply for MFU""")
    v_Q23 = st.radio('easy/convenient transportation', ['Yes', 'No'])
    v_Q24 = st.radio('suitable cost ', ['Yes', 'No'])
    v_Q25 = st.radio('graduates with higher language/academic competency than other universities', ['Yes', 'No'])
    v_Q26 = st.radio('learning in English', ['Yes', 'No'])
    v_Q27 = st.radio('quality/reputation of university', ['Yes', 'No'])
    v_Q28 = st.radio('excellence in learning support and facilities', ['Yes', 'No'])
    v_Q30 = st.radio('environment and setting motivate learning', ['Yes', 'No'])
    v_Q31 = st.radio('experienced and high-quality instructors', ['Yes', 'No'])
    v_Q32 = st.radio('suggestion by school teacher/friend/relative', ['Yes', 'No'])
    v_Q33 = st.radio('suggestion by family', ['Yes', 'No'])

    

    if v_FacultyID == 'School of Liberal Arts': v_FacultyID = 10 
    elif v_FacultyID == 'School of Science': v_FacultyID = 11
    elif v_FacultyID == 'School of Management': v_FacultyID = 12
    elif v_FacultyID == 'School of Information Technology': v_FacultyID = 13
    elif v_FacultyID == 'School of Agro-industry': v_FacultyID = 14
    elif v_FacultyID == 'School of Law': v_FacultyID = 16
    elif v_FacultyID == 'School of Cosmetic Science': v_FacultyID = 17
    elif v_FacultyID == 'School of Health Science': v_FacultyID = 18
    elif v_FacultyID == 'School of Nursing': v_FacultyID = 19
    elif v_FacultyID == 'School of Medicine': v_FacultyID = 21
    elif v_FacultyID == 'School of Dentistry': v_FacultyID = 22
    elif v_FacultyID == 'School of Social Innovation': v_FacultyID = 23
    elif v_FacultyID == 'School of Sinology': v_FacultyID = 24
    else: v_FacultyID = 25

    if v_DepartmentCode == 'School of Liberal Arts': v_DepartmentCode = 1006 
    elif v_DepartmentCode == 'Applied Chemistry': v_DepartmentCode = 1102
    elif v_DepartmentCode == 'Biotechnology': v_DepartmentCode = 1105
    elif v_DepartmentCode == 'Materials Engineering': v_DepartmentCode = 1112
    elif v_DepartmentCode == 'Accounting': v_DepartmentCode = 1201
    elif v_DepartmentCode == 'Economics': v_DepartmentCode = 1202
    elif v_DepartmentCode == 'Business Administration': v_DepartmentCode = 1203
    elif v_DepartmentCode == 'Tourism Management': v_DepartmentCode = 1205
    elif v_DepartmentCode == 'Hospitality Industry Management': v_DepartmentCode = 1207
    elif v_DepartmentCode == 'Logistics and Supply Chain Management': v_DepartmentCode = 1209
    elif v_DepartmentCode == 'Aviation Business Management': v_DepartmentCode = 1210
    elif v_DepartmentCode == 'Information Technology': v_DepartmentCode =1301
    elif v_DepartmentCode == 'Computer Science and Innovation': v_DepartmentCode = 1302
    elif v_DepartmentCode == 'Software Engineering': v_DepartmentCode = 1305
    elif v_DepartmentCode == 'Multimedia Technology and Animation': v_DepartmentCode = 1306
    elif v_DepartmentCode == 'Food Science and Technology': v_DepartmentCode = 1401
    elif v_DepartmentCode == 'Posthavest Technology and Logistics': v_DepartmentCode = 1407
    elif v_DepartmentCode == 'Computer Engineering': v_DepartmentCode = 1501
    elif v_DepartmentCode == 'Laws': v_DepartmentCode = 1601
    elif v_DepartmentCode == 'Cosmetic Science': v_DepartmentCode = 1701
    elif v_DepartmentCode == 'Beauty Technology': v_DepartmentCode = 1703
    elif v_DepartmentCode == 'Public Health': v_DepartmentCode = 1804
    elif v_DepartmentCode == 'Sports and Health Science': v_DepartmentCode = 1806
    elif v_DepartmentCode == 'Environmental Health': v_DepartmentCode = 1807
    elif v_DepartmentCode == 'Occupational Health and Safety': v_DepartmentCode =1808
    elif v_DepartmentCode == 'Nursing Science': v_DepartmentCode = 1901
    elif v_DepartmentCode == 'Medicine': v_DepartmentCode = 2101
    elif v_DepartmentCode == 'Dentistry': v_DepartmentCode = 2201
    elif v_DepartmentCode == 'International Development': v_DepartmentCode = 2301
    elif v_DepartmentCode == 'Chinese Study': v_DepartmentCode = 2401
    elif v_DepartmentCode == 'Business Chinese': v_DepartmentCode =2402
    elif v_DepartmentCode == 'Teaching Chinese Language (5 Year)': v_DepartmentCode = 2403
    elif v_DepartmentCode == 'Chinese Language and Culture': v_DepartmentCode = 2404
    elif v_DepartmentCode == 'Applied Thai Traditional Medicine': v_DepartmentCode = 2501
    elif v_DepartmentCode == 'Physical Therapy': v_DepartmentCode =2502
    else: v_DepartmentCode = 2503

    if v_HomeRegion == 'North': v_HomeRegion = 1 
    else: v_HomeRegion = 0

    if v_SchoolRegion == 'North': v_SchoolRegion = 1 
    else: v_SchoolRegion = 0

    if v_TCAS == '1': v_TCAS = 1
    elif v_TCAS == '2': v_TCAS = 2
    else: v_TCAS = 5

    if v_EntryTypeID == 'Quota 17 northern provinces': v_EntryTypeID = 10
    elif v_EntryTypeID == 'Direct admission by school': v_EntryTypeID = 29
    elif v_EntryTypeID == 'Direct admission': v_EntryTypeID = 20
    elif v_EntryTypeID == 'Special for good student': v_EntryTypeID = 52
    else: v_EntryTypeID = 11

    if v_Q1 == 'Yes': v_Q1 = 1 
    else: v_Q1 = 0

    if v_Q3 == 'Yes': v_Q3 = 1 
    else: v_Q3 = 0

    if v_Q4 == 'Yes': v_Q4 = 1 
    else: v_Q4 = 0

    if v_Q5 == 'Yes': v_Q5 = 1 
    else: v_Q5 = 0

    if v_Q6 == 'Yes': v_Q6 = 1 
    else: v_Q6 = 0

    if v_Q8 == 'Yes': v_Q8 = 1 
    else: v_Q8 = 0

    if v_Q9 == 'Yes': v_Q9 = 1 
    else: v_Q9 = 0

    if v_Q12 == 'Yes': v_Q12 = 1 
    else: v_Q12 = 0

    if v_Q13 == 'Yes': v_Q13 = 1 
    else: v_Q13 = 0

    if v_Q19 == 'Yes': v_Q19 = 1 
    else: v_Q19 = 0

    if v_Q20 == 'Yes': v_Q20 = 1 
    else: v_Q20 = 0

    if v_Q21 == 'Yes': v_Q21 = 1 
    else: v_Q21 = 0

    if v_Q23 == 'Yes': v_Q23 = 1 
    else: v_Q23 = 0

    if v_Q24 == 'Yes': v_Q24 = 1 
    else: v_Q24 = 0

    if v_Q25 == 'Yes': v_Q25 = 1 
    else: v_Q25 = 0

    if v_Q26 == 'Yes': v_Q26 = 1 
    else: v_Q26 = 0

    if v_Q27 == 'Yes': v_Q27 = 1 
    else: v_Q27 = 0

    if v_Q28 == 'Yes': v_Q28 = 1 
    else: v_Q28 = 0

    if v_Q30 == 'Yes': v_Q30 = 1 
    else: v_Q30 = 0

    if v_Q31 == 'Yes': v_Q31 = 1 
    else: v_Q31 = 0

    if v_Q32 == 'Yes': v_Q32 = 1 
    else: v_Q32 = 0

    if v_Q33 == 'Yes': v_Q33 = 1 
    else: v_Q33 = 0




    #dictionary
    data = {'FacultyID': v_FacultyID,
            'DepartmentCode': v_DepartmentCode,
            'EntryTypeID': v_EntryTypeID,
            'TCAS': v_TCAS,
            'HomeRegion': v_HomeRegion,
            'SchoolRegionNameEng': v_SchoolRegion,
            'EntryGPA': v_EntryGPA,
            'GPAX': v_GPAX,
            'GPA_Eng': v_GPA_Eng,
            'GPA_Math': v_GPA_Math,
            'GPA_Sci': v_GPA_Sci,
            'GPA_Sco': v_GPA_Sco,
            'Q1': v_Q1,
            'Q3': v_Q3,
            'Q4': v_Q4,
            'Q5': v_Q5,
            'Q6': v_Q6,
            'Q8': v_Q8,
            'Q9': v_Q9,
            'Q12': v_Q12,
            'Q13': v_Q13,
            'Q19': v_Q19,
            'Q20': v_Q20,
            'Q21': v_Q21,
            'Q23': v_Q23,
            'Q24': v_Q24,
            'Q25': v_Q25,
            'Q26': v_Q26,
            'Q27': v_Q27,
            'Q28': v_Q28,
            'Q30': v_Q30,
            'Q31': v_Q31,
            'Q32': v_Q32,
            'Q33': v_Q33}

    #create data frame
    data_df = pd.DataFrame(data, index=[0])
    return data_df

df = get_input()
st.write("""## Input Value""")
st.write(df)
data_sample = pd.read_csv('S_thai_female_tcas.csv')
X_new = df
X_new = X_new[:1] # Select only the first row (the user input data)
load_nor = pickle.load(open('normalization.pkl', 'rb'))
X_new = load_nor.transform(X_new)
st.write("""## Input Value After Normalization""")
st.write(X_new)
# -- Reads the saved classification model
load_knn = pickle.load(open('best_knn.pkl', 'rb'))
# Apply model for prediction
prediction = load_knn.predict(X_new)
st.write("""## Prediction Results""")
st.write(prediction)

