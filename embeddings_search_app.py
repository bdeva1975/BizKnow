import streamlit as st
import embeddings_search_lib as glib
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Embeddings Search", layout="wide")
st.title("Embeddings Search")

input_text = st.text_input("Enter your question:")
go_button = st.button("Search", type="primary")

if go_button:
    with st.spinner("Searching..."):
        response_content = glib.get_similarity_search_results(question=input_text)
        
        if response_content:
            st.subheader("Search Results:")
            for i, result in enumerate(response_content, 1):
                st.markdown(f"**Result {i}:**")
                st.write(result)
                st.markdown("---")
        else:
            st.warning("No results found. Please try a different question.")

# Add a footer with information about the embeddings being used
st.markdown("---")
st.markdown("*This search uses OpenAI embeddings and a local document collection.*")