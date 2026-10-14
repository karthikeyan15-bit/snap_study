import streamlit as st

from gemini_service import analyze_image


st.set_page_config(
    page_title="Snap & Study",
    page_icon="📸",
    layout="centered"
)


st.title("📸 Snap & Study")

st.subheader(
    "Snap it. Study it. Understand it."
)

st.write(
    "Take a photo or upload an image of "
    "a question, notes, diagram or code."
)


mode = st.selectbox(
    "What should Snap & Study do?",
    [
        "Explain",
        "Solve",
        "Summarize",
        "Quiz Me"
    ]
)


input_method = st.radio(
    "Choose input method",
    [
        "📷 Take a photo",
        "📁 Upload an image"
    ]
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


    if st.button(
        "🔍 Analyze with Snap & Study",
        type="primary"
    ):

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

                st.session_state["last_result"] = result

            except Exception as e:

                st.error(
                    "Something went wrong."
                )

                st.exception(e)
