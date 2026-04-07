import streamlit as st
import base64
import time

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
p, span, div, label, small,
.stMarkdown, .stText {{
    color: white !important;
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
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ----------- Title -----------
st.markdown("<h1 style='text-align:center;'>🤖 NSTIW Smart Assistant</h1>", unsafe_allow_html=True)
st.markdown("Welcome! Ask anything about NSTIW 💬")

# ----------- Chat History -----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------- Display Chat -----------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user", avatar="😊"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(msg["content"])

# ----------- User Input -----------
user = st.chat_input("Type your message here...")

if user:
    user_lower = user.lower()

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user})
    with st.chat_message("user", avatar="😊"):
        st.markdown(user)

    # ----------- Bot Logic ---------------
    response = ""

    if "hi" in user_lower or "hey" in user_lower or "hello" in user_lower:
        response = "NSTI: Hey there! How may help you?"
        
    elif "about" in user_lower and "nstiw" in user_lower and "allahabad" in user_lower:
        response = "NSTI: National Skill Training Institute (Women), Allahabad bring carrier opprtunities for women to make them independent. For more informations:👉 https://nstiwallahabad.dgt.gov.in/"
        
    elif "location" in user_lower and "nsti" in user_lower:
        response = "NSTI: https://maps.app.goo.gl/kr6mpTcgBsctztzx9"
        
    elif "timing" in user_lower:
        response = "NSTI: Institute opens from 9am to 5:30pm and there is official holidays on saturdays and sundays."
        
    elif "hostel" in user_lower and "facilities" in user_lower:
        response = "NSTI: Hostel facilities are very good. link: https://nstiwallahabad.dgt.gov.in/en/manage-hostel"
        
    elif "fee structure" in user_lower and "nsti" in user_lower:
        response = "NSTI: Fee is very affordable as you can check here 👉: https://nstiwallahabad.dgt.gov.in/en/fee-structure"
        
    elif "alumni" in user_lower and "nsti" in user_lower:
        response = "NSTI: many alumni has passed. you can check here 👉: https://nstiwallahabad.dgt.gov.in/en/alumni"
        
    elif "staff" in user_lower and "present" in user_lower and "nsti" in user_lower:
        response = "NSTI: There are so many staffs are present including guest facility. click here 👉: https://nstiwallahabad.dgt.gov.in/all-staff-profiles"
        
    elif "admission" in user_lower and "cits" in user_lower and "open" in user_lower:
        response = "NSTI: Admissions for CITS courses are starts from 18th of April."
        
    elif "admission" in user_lower and "cts" in user_lower and "open" in user_lower:
        response = "NSTI: Admissions for CTS courses are starts from May."
        
    elif "where" in user_lower and "nstiw" in user_lower and "located" in user_lower:
        response = "NSTI: It is located in 6, New Katra, Prayagraj."
        
    elif "courses" in user_lower and "nsti" in user_lower:
        response = "NSTI: COPA, CSA, AIPA, EM, COSMO, DM, FDT, OM, C&H are the major courses. For more information click link: https://nstiwallahabad.dgt.gov.in/en/cts"
        
    elif "aipa" in user_lower and "duration" in user_lower:
        response = "NSTI: It is a CTS course for 1 year with Eligibility 10th pass"
        
    elif "aipa" in user_lower and "information" in user_lower:
        response = "NSTI: The Artificial Intelligence Programming Assistant (AIPA) is a one-year, DGT-certified, National Trade Certificate (NTC) program designed to teach foundational AI, Python programming, machine learning, and generative AI skills"
        
    elif "process" in user_lower and "selection" in user_lower and "cts" in user_lower:
        response = "NSTI: Selection is based on merit calculated from marks obtained in the 10th class examination."
        
    elif "process" in user_lower and "selection" in user_lower and "cits" in user_lower:
        response = "NSTI: The CITS selection process at NSTIs involves passing the All India Common Entrance Test (AICET), typically conducted online by DGT/NIMI in June/July."
        
    elif "connect" in user_lower and "nsti" in user_lower:
        response = "NSTI: You can connect us through 👉 Phone (Office): 0532-2971803, Email: nstiwallahabad@gmail.com or nstiw-allahabad@dgt.gov.in."
        
    elif "bye" in user_lower:
        response = "Bye! Take care 👋"
        
    else:
        response = "NSTI: I didn't understand."

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