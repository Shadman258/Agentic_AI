
import streamlit as st
from youtube_analyzer import build_youtube_agent


# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="AI YouTube Analyzer",
    page_icon="🎥",
    layout="wide"
)


# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>

.stApp{
background:
linear-gradient(
135deg,
#070B14,
#101B30,
#0D1117
);
color:white;
}

/* Hero */
.hero{
padding:45px;
border-radius:28px;

background:
linear-gradient(
135deg,
rgba(255,255,255,.08),
rgba(255,255,255,.03)
);

backdrop-filter:blur(30px);

border:1px solid rgba(255,255,255,.15);

text-align:center;

margin-bottom:25px;
}

.hero h1{
font-size:52px;
font-weight:800;
}

.hero p{
font-size:20px;
color:#B5BFD3;
}

/* Input */

.stTextInput>div>div>input{
border-radius:18px;
padding:18px;
font-size:18px;
}

/* Button */

.stButton button{
width:100%;
height:60px;

border:none;

border-radius:18px;

background:
linear-gradient(
90deg,
#FF416C,
#FF4B2B
);

color:white;

font-size:20px;

font-weight:700;
}

.stButton button:hover{
transform:scale(1.02);
}


/* Result Card */

.result{

padding:40px;

border-radius:25px;

background:
rgba(255,255,255,.05);

border:
1px solid rgba(255,255,255,.1);

backdrop-filter:
blur(30px);

margin-top:30px;

}

</style>
""", unsafe_allow_html=True)


# -------------------------
# HEADER
# -------------------------

st.markdown("""
<div class="hero">

<h1>🎥 AI YouTube Analyzer</h1>

<p>
Analyze any YouTube video with
⚡ AI • 🧠 Smart Summary • ⏱ Timestamps
</p>

</div>
""", unsafe_allow_html=True)


# -------------------------
# LOAD AGENT
# -------------------------

@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()


# -------------------------
# INPUT
# -------------------------

video_url = st.text_input(
    "YouTube Video URL",
    placeholder="📎 Paste YouTube URL...",
    label_visibility="collapsed"
)


analyze = st.button(
    "🚀 Analyze Video"
)


# -------------------------
# ANALYSIS
# -------------------------

if analyze and video_url:

    try:

        st.video(video_url)

        progress = st.progress(0)

        for i in range(100):

            progress.progress(i+1)

        with st.spinner(
            "🧠 AI is analyzing the video..."
        ):

            response = agent.run(
                f"""
Analyze this video:

{video_url}

Make the output beautiful.
"""
            )

        progress.empty()

        st.markdown(
            """
<div class="result">
<h2>
📊 Analysis Report
</h2>
</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            response.content
        )

        st.success(
            "✨ Analysis Completed"
        )

        st.balloons()

    except Exception as e:

        st.error(
            f"❌ Error: {e}"
        )


# -------------------------
# FOOTER
# -------------------------

st.markdown("---")

st.caption(
"Built with ❤️ • Streamlit • Groq • Qwen3-32B"
)
