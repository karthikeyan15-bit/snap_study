import streamlit as st

from gemini_service import analyze_image


st.set_page_config(
    page_title="Snap & Study",
    page_icon="📸",
    layout="centered",
    initial_sidebar_state="expanded"
)


st.title("📸 Snap & Study")

st.subheader(
    "Snap it. Study it. Understand it."
)

st.write(
    "Take a photo or upload an image of "
    "a question, notes, diagram or code."
)


with st.sidebar:
    st.header("⚙️ Settings")

    mode = st.selectbox(
        "What should Snap & Study do?",
        [
            "Explain",
            "Solve",
            "Summarize",
            "Quiz Me"
        ],
        index=0
    )

    st.divider()

    if st.button("🗑️ Clear History", use_container_width=True):
        if "history" in st.session_state:
            st.session_state.history = []
        st.rerun()

    st.divider()
    st.caption("Powered by Gemini 3.5 Flash-Lite")


input_method = st.radio(
    "Choose input method",
    [
        "📷 Take a photo",
        "📁 Upload an image"
    ],
    horizontal=True
)


image = None

if input_method == "📷 Take a photo":

    image = st.camera_input(
        "Take a picture"
    )

else:

    image = st.file_uploader(
        "Upload your image",
        type=[
            "jpg",
            "jpeg",
            "png",
            "webp"
        ]
    )


if image:

    st.image(
        image,
        caption="Your study material",
        use_container_width=True
    )

    col1, col2 = st.columns([3, 1])
    with col1:
        analyze_btn = st.button(
            "🔍 Analyze with Snap & Study",
            type="primary",
            use_container_width=True
        )
    with col2:
        if "last_result" in st.session_state:
            if st.button("📋 Copy", use_container_width=True):
                st.toast("Copied to clipboard!")

    if analyze_btn:

        with st.spinner(
            "🧠 Snap & Study is analyzing..."
        ):

            try:

                result = analyze_image(
                    image,
                    mode
                )

                st.success(
                    "Analysis complete!"
                )

                st.markdown(
                    "## 🤖 Snap & Study"
                )

                st.markdown(
                    result
                )

                if "history" not in st.session_state:
                    st.session_state.history = []

                st.session_state.history.append({
                    "mode": mode,
                    "result": result,
                    "image": image
                })
                st.session_state["last_result"] = result

            except Exception as e:

                st.error(
                    "Something went wrong."
                )

                st.exception(e)


if "history" in st.session_state and st.session_state.history:
    st.divider()
    st.subheader("📜 History")

    for idx, item in enumerate(reversed(st.session_state.history)):
        with st.expander(f"{item['mode']} - {len(st.session_state.history) - idx}"):
            st.markdown(item["result"])