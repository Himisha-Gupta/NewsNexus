# app.py
import streamlit as st
from crew import run_crew

def main():
    # Set up the Streamlit app layout
    st.title("News Nexus: Intelligent Agent")
    st.markdown(
        """
        Discover the cutting edge of technology and AI with our 
        News Nexus: Intelligent Agent. 
        Dive into in-depth research and captivating articles 
        that keep you at the forefront of innovation.
        """
    )

    # Sidebar for task selection
    st.sidebar.header("Choose a Task")
    task = st.sidebar.radio("Select Task", ["Research", "Write"])
    topic = st.text_input("Enter the topic you want to explore", "")

    # Handle the selected task
    if task == "Research":
        if st.button("Start Research"):
            if topic:
                with st.spinner("Researching..."):
                    result = run_crew(task_type='research', topic=topic)
                    st.subheader("Research Findings")
                    st.write(result)
            else:
                st.error("Please enter a topic to research.")
    
    elif task == "Write":
        if st.button("Start Writing"):
            if topic:
                with st.spinner("Writing article..."):
                    result = run_crew(task_type='write', topic=topic)
                    st.subheader("Article")
                    st.markdown(result)
            else:
                st.error("Please enter a topic to write about.")

# Run the app
if __name__ == "__main__":
    main()
