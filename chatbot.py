import streamlit as st
import base64
import time


# ----------- Analytics -----------
if "query_count" not in st.session_state:
    st.session_state.query_count = 0

# ----------- Rules & Regulations Box -----------
st.sidebar.markdown("## 📜 Rules & Regulations")

with st.sidebar.expander("Click to View Rules 👇"):

    st.markdown("""
    ### 📌 Important Rules:

    - 🎓 **Attendance:** Minimum 80% attendance is mandatory.
    - 👕 **Uniform:** Proper uniform must be worn daily.
    - 🪪 **ID Card:** Carry ID card inside campus.
    - ⚖ **Discipline:** Maintain discipline and respect faculty.
    - 📝 **Exams:** Follow all exam rules strictly.
    - 📅 **Leave:** Take permission before leave.
    - 📵 **Mobile Usage:** Avoid mobile during class hours.
    - 🧹 **Cleanliness:** Keep campus clean.
    - 🔐 **Security:** Follow safety guidelines at all times.
    """)


# ----------- Page Config -----------
st.set_page_config(page_title="NSTIW Chatbot", page_icon="🤖", layout="centered")

# ----------- Function to Load Local Image -----------
def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ----------- Load Background Image -----------
bg_img = get_base64("nsti.jpg")  
# ----------- Custom CSS (Glass UI + White Text) -----------
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{bg_img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

/* Dark overlay */
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.6);
}}

/* Header transparent */
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

/* FORCE ALL TEXT WHITE */
h1, h2, h3, h4, h5, h6,
p, span, label, small,
.stMarkdown, .stText {{
    color: black !important;
}}

/* Chat messages */
[data-testid="stChatMessage"] {{
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    padding: 10px;
    border-radius: 15px;
    margin-bottom: 10px;
    color: white !important;
}}

/* Chat input box text BLACK */
textarea, input {{
    color: black !important;
    background: rgba(255,255,255,0.9) !important;
    border-radius: 10px !important;

}}
/* Placeholder also black */
textarea::placeholder {{
    color: #333 !important;
}}


/* Fix Streamlit specific text */
[data-testid="stMarkdownContainer"] * {{
    color: white !important;
}}


/* Smart Suggestion Buttons Styling */
div.stButton > button {{
    background-color: #6f42c1 !important;   /* green */
    color: white !important;                /* text white */
    border-radius: 10px !important;
    border: none;
    padding: 10px 15px;
    font-weight: bold;
}}

/* Hover effect */
div.stButton > button:hover {{
    background-color: #45a049 !important;
    color: white !important;
}}

[data-testid="stSidebar"] {{
    background: rgba(255,255,255,0.2) !important;
    backdrop-filter: blur(10px);
}}

[data-testid="stSidebar"] * {{
    color: white !important;
}}

/* Rules box styling */
details {{
    background: rgba(255,255,255,0.2);
    padding: 10px;
    border-radius: 10px;
    color: white;
}}


</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ----------- Title -----------
st.markdown("<h1 style='text-align:center;'>🤖 NSTIW Smart Assistant</h1>", unsafe_allow_html=True)
st.markdown("Welcome! Ask anything about NSTIW 💬")



# ----------- SIDEBAR DASHBOARD -----------
st.sidebar.title("📊 Smart Dashboard")

# 📈 Analytics
st.sidebar.subheader("📈 Analytics")
st.sidebar.write("Total Queries:", st.session_state.query_count)


# 🎯 Smart Info Cards (Sidebar Version)
st.sidebar.subheader("🎯 Quick Access")

if st.sidebar.button("📚 Courses"):
    st.sidebar.success("Courses: COPA, CSA, AIPA, EM, FDT etc.")

if st.sidebar.button("💰 Fees"):
    st.sidebar.success("Fee is affordable. Check official website.")

if st.sidebar.button("🏠 Hostel"):
    st.sidebar.success("Hostel available with mess & facilities.")

if st.sidebar.button("📍 Location"):
    st.sidebar.success("NSTI, New Katra, Prayagraj.click here:https://maps.app.goo.gl/kr6mpTcgBsctztzx9")

if st.sidebar.button("📞 Contact"):
    st.sidebar.success("Phone: 0532-2971803")

if st.sidebar.button("💼 Placement"):
    st.sidebar.success("Placement support available.")

# 💡 Did You Know
st.sidebar.subheader("💡 Did You Know?")
st.sidebar.info("NSTI courses are designed to make students industry-ready.")

# ----------- User Personalization -----------
name = st.text_input("Enter your name 😊")
if name:
    st.success(f"Welcome {name} 🎉" )

# ----------- AI Mode -----------
ai_mode = st.toggle("🤖 Smart AI Mode")

# ----------- Smart Suggestions -----------
st.write("💡 Quick Help:")
col1, col2, col3 = st.columns(3)

suggestion = None
if col1.button("Courses"):
    suggestion = "courses"
elif col2.button("Fees"):
    suggestion = "fee structure nsti"
elif col3.button("Hostel"):
    suggestion = "hostel facilities nsti"

# ----------- Chat History -----------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="😊" if msg["role"]=="user" else "🤖"):
        st.markdown(msg["content"])

# ----------- Single Input ONLY -----------
user_input = st.chat_input("Type your message here...")

# Priority: button click OR typing
user = suggestion if suggestion else user_input

# ----------- Process Input -----------
if user:
    st.session_state.query_count += 1

    user_lower = user.lower()

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user})
    with st.chat_message("user", avatar="😊"):
        st.markdown(user)

# ----------- AI Mode Response -----------
    if ai_mode and user:
        response = f"🤖 AI Mode Active: Sorry {name if name else ''}, I will soon provide intelligent answers!"

    else:

    # ----------- Bot Logic ---------------
        response = ""

    if "hi" in user_lower or "hey" in user_lower or "hello" in user_lower:
        response = f"NSTI: Hey {name if name else 'there'}! How may I help you?"
        
    elif  "nstiw" in user_lower and "allahabad" in user_lower:
        response = "NSTI: National Skill Training Institute (Women), Allahabad bring carrier opprtunities for women to make them independent. For more informations:👉 https://nstiwallahabad.dgt.gov.in/"
        
    elif "location" in user_lower:
        response = "NSTI: https://maps.app.goo.gl/kr6mpTcgBsctztzx9"
        
    elif "timing" in user_lower:
        response = "NSTI: Institute opens from 9am to 5:30pm and there is official holidays on saturdays and sundays."

    elif "holiday" in user_lower:
        response = "NSTI: Holidays are provided as per government and institute calendar."

    elif "syllabus" in user_lower:
        response = "NSTI: Syllabus is designed by DGT and includes both theory and practical."

    elif "project" in user_lower:
        response = "NSTI: Students are required to complete projects for practical learning."

    elif "marks" in user_lower:
        response = "NSTI: Marks are based on theory exams, practicals, and internal assessment."

    elif "fail" in user_lower:
        response = "NSTI: Students may get chance to reappear in exams if they fail."
        
    elif "hostel" in user_lower:
        response = "NSTI: Hostel facilities are very good. link: https://nstiwallahabad.dgt.gov.in/en/manage-hostel"

    elif "food" in user_lower or "mess" in user_lower:
        response = "NSTI: Hostel provides mess facilities with regular meals."

    elif "room" in user_lower:
        response = "NSTI: Hostel rooms are shared and equipped with basic facilities."

    elif "water" in user_lower:
        response = "NSTI: Clean drinking water is available in hostel and campus."

    elif "electricity" in user_lower:
        response = "NSTI: Proper electricity supply is available with backup facilities."

    elif "fee structure" in user_lower:
        response = "NSTI: Fee is very affordable as you can check here 👉: https://nstiwallahabad.dgt.gov.in/en/fee-structure"
        
    elif "alumni" in user_lower:
        response = "NSTI: many alumni has passed. you can check here 👉: https://nstiwallahabad.dgt.gov.in/en/alumni"
        
    elif "job" in user_lower:
        response = "NSTI: Courses are skill-based and help students get job opportunities in various industries."

    elif "salary" in user_lower:
        response = "NSTI: Salary depends on skills, role, and company after course completion."

    elif "future" in user_lower:
        response = "NSTI: Students can pursue jobs, higher studies, or entrepreneurship after completing courses."

    elif "government job" in user_lower:
        response = "NSTI: NSTI certification can help in applying for various government jobs."

    elif "skills" in user_lower:
        response = "NSTI: Students gain technical and practical skills for real-world applications."

    elif "lab" in user_lower:
        response = "NSTI: Well-equipped labs are available for practical training."

    elif "sports" in user_lower:
        response = "NSTI: Sports and extracurricular activities are encouraged."

    elif "medical" in user_lower:
        response = "NSTI: Basic medical support may be available in case of emergency."

    elif "security" in user_lower:
        response = "NSTI: Campus has proper security for student safety."

    elif "staffs" in user_lower:
        response = "NSTI: There are so many staffs are present including guest facility. click here 👉: https://nstiwallahabad.dgt.gov.in/all-staff-profiles"
        
    elif "admission" in user_lower and "cits" in user_lower:
        response = "NSTI: Admissions for CITS courses are starts from 18th of April."
        
    elif "admission" in user_lower and "cts" in user_lower:
        response = "NSTI: Admissions for CTS courses are starts from May."
        
    elif "where" in user_lower and "nstiw" in user_lower and "located" in user_lower:
        response = "NSTI: It is located in 6, New Katra, Prayagraj."
        
    elif "courses" in user_lower:
        response = "NSTI: COPA, CSA, AIPA, EM, COSMO, DM, FDT, OM, C&H are the major courses. For more information of cts: https://nstiwallahabad.dgt.gov.in/en/cts " \
        "CITS:https://nstiwallahabad.dgt.gov.in/en/cits"
        
    elif "aipa" in user_lower and "duration" in user_lower:
        response = "NSTI: It is a CTS course for 1 year with Eligibility 10th pass"
        
    elif "aipa" in user_lower and "information" in user_lower:
        response = "NSTI: The Artificial Intelligence Programming Assistant (AIPA) is a one-year, DGT-certified, National Trade Certificate (NTC) program designed to teach foundational AI, Python programming, machine learning, and generative AI skills"
        
    elif "process" in user_lower or "selection" in user_lower and "cts" in user_lower:
        response = "NSTI: Selection is based on merit calculated from marks obtained in the 10th class examination."
        
    elif "process" in user_lower or "selection" in user_lower and "cits" in user_lower:
        response = "NSTI: The CITS selection process at NSTIs involves passing the All India Common Entrance Test (AICET), typically conducted online by DGT/NIMI in June/July."
        
    elif "connect" in user_lower and "nsti" in user_lower:
        response = "NSTI: You can connect us through 👉 Phone (Office): 0532-2971803, Email: nstiwallahabad@gmail.com or nstiw-allahabad@dgt.gov.in."

    elif "placement" in user_lower:
        response = "NSTI: Placement support is provided. Many students get opportunities in industries and startups after completing courses."

    elif "internship" in user_lower:
        response = "NSTI: Yes, students may get internship opportunities depending on their course and performance."


    elif "discipline" in user_lower:
        response = "NSTI: Students must maintain discipline and follow institute rules at all times."

    elif "leave" in user_lower:
        response = "NSTI: Leave can be taken with prior permission from the instructor."

    elif "id card" in user_lower:
        response = "NSTI: Students must carry ID cards daily inside the campus."

    elif "dress" in user_lower:
        response = "NSTI: Proper dress code or uniform is required depending on the trade."

    elif "uniform" in user_lower and "cts" in user_lower:
        response ="NSTI: Uniform for cts is usually a black trouser and white shirt"
    
    elif "uniform" in user_lower and "cits" in user_lower:
        response ="NSTI: Uniform for cits is usually a navy blue trouser and sky blue shirt"

    elif "attendance" in user_lower:
        response = "NSTI: Minimum 80% attendance is must be required to appear in exams."

    elif "exam" in user_lower:
        response = "NSTI: Exams are conducted yearly under DGT guidelines."

    elif "certificate" in user_lower:
        response = "NSTI: After completion, students receive a National Trade Certificate (NTC)."

    elif "practical" in user_lower:
        response = "NSTI: Courses include both theoretical and practical training for skill development."

    elif "teacher" in user_lower:
        response = "NSTI: Trainers are experienced and supportive, including guest faculty."

    elif "safety" in user_lower:
        response = "NSTI: The campus is safe and secure for women with proper facilities."

    elif "wifi" in user_lower:
        response = "NSTI: Limited internet/WiFi facilities may be available for academic use."

    elif "nervous" in user_lower:
        response = "NSTI: It's okay to feel nervous 😊 You will learn step by step and gain confidence!"

    elif "difficult" in user_lower:
        response = "NSTI: Courses may feel challenging at first, but with practice, it becomes easier."

    elif "friends" in user_lower:
        response = "NSTI: You will meet many new friends and build a strong network here!"

    elif "first day" in user_lower:
        response = "NSTI: On your first day, you will be introduced to your course, teachers, and campus."

    elif "help" in user_lower:
        response = "NSTI: I’m always here to help 😊 You can ask me anything about NSTI!"

    elif "why should i join nsti" in user_lower:
        response = "NSTI: NSTI provides skill-based training, experienced faculty, practical exposure, and career opportunities, making students job-ready."

    elif "bye" in user_lower:
        response = "Bye! Take care 👋"

    else:
        response = f"NSTI: Sorry {name if name else ''}, I didn’t understand. You can ask about courses, fees, hostel, or admissions 😊"

    # ----------- Typing Effect -----------
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        full_text = ""
        
        for char in response:
            full_text += char
            time.sleep(0.01)
            message_placeholder.markdown(full_text + "▌")
        
        message_placeholder.markdown(full_text)

